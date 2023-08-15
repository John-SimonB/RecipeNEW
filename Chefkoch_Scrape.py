import requests
from bs4 import BeautifulSoup
#### Die folgende Funktion lädt alle Rezeptinformationen von "Chefkoch"
#### Dafür wird der HTML text durchsucht und einzelne benötigte Informationen extrahiert.
#### PARAMETER:
#### URL = Rezeptlink von Chefkoch
#### RETURN: 
#### products = Alle Informationen des Rezeptes
#### QUELLEN:
#### https://www.youtube.com/watch?v=-u4GyvpQZBU
#### https://www.chefkoch.de
#### https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#### https://www.youtube.com/watch?v=IFJq_cXR2lU
#### CHAT-GPT
def chefkoch_scrape(URL):
    if "https://www.chefkoch.de/rezepte/" in URL:
        response = requests.get(URL, timeout=3)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser') 
            name = soup.find("h1").text.strip()
            products = []

            subtitle_element = soup.find("p", class_="recipe-text")
            if subtitle_element:
                subtitle = subtitle_element.text.strip()
            else:
                subtitle = ""
            if soup.find(class_="ds-box recipe-author bi-recipe-author"):
                element = soup.find(class_="ds-box recipe-author bi-recipe-author")
                span_element = element.find('span').text.strip().split()
                author = span_element[len(span_element) -1 ]


            image_element = soup.find("img", class_="i-amphtml-fill-content i-amphtml-replaced-content")
            if image_element:
                image_src = image_element["src"]

            products.append(name) ## Name des Rezeptes
            products.append(author) ## Autor des Rezeptes
            products.append(image_src) ## Bild vom Rezept
            products.append(subtitle) ## Untertitel des Rezeptes
            td_left_elements = soup.find_all("td", class_="td-left")
            td_right_elements = soup.find_all("td", class_="td-right")

            td_left_contents = [td_left.text.strip() for td_left in td_left_elements]
            td_right_contents = [td_right.text.strip() for td_right in td_right_elements]

            td_left_contents = [content.strip().replace(" ", "") if content.strip() != "" else "0g" for content in td_left_contents]
            td_right_contents = [content.strip().replace(",", "") if content.strip() != "" else "" for content in td_right_contents]

            data = []
            for i in range(min(len(td_left_contents), len(td_right_contents))):
                left_content = td_left_contents[i]
                right_content = td_right_contents[i]
                if any(char.isalpha() for char in left_content):
                    if left_content != "0g":
                        amount = "".join(filter(str.isdigit, left_content)).replace(",", ".")
                        unit = "".join(filter(str.isalpha, left_content))
                    if "½" in left_content:
                        amount = "0.5"
                        unit = "".join(filter(str.isalpha, left_content))
                    else:
                        amount = "".join(filter(str.isdigit, left_content)).replace(",", ".")
                        if amount == "0":
                            unit == "X"
                        unit = "".join(filter(str.isalpha, left_content))
                        if(unit.lower() == "etwas" or unit == "Pck" or unit == "nb" or unit == "ein wenig" or unit == "prise" or unit == "ungefähr" or unit == "handvoll" or unit == "0" or unit == "" or unit == "evtl" or unit == "große"):
                            unit = "X"
                else:
                    amount, unit = "".join(filter(str.isdigit, left_content)), "X"
                if(amount == "0"):
                    unit = "X"
                product = [right_content, amount, unit]
                data.append(product) ## Benötigtes Produkt
            products.append(data) ## Alle benötigten Produkte

            input_element = soup.find('input', {'name': 'portionen'})

            if input_element:
                portion = input_element.get('value')
                products.append(portion) ## Portionsgröße
            else:
                print("value not found")
            print(products)
            return products
    else:
        return False

#Beispielaufruf
#url = "https://www.chefkoch.de/rezepte/2917311444051618/Bester-und-leckerster-Nudelsalat.html"
#print(chefkoch_scrape(url))

