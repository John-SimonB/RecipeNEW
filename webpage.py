from flask import Flask, redirect, url_for, render_template, request
from LoadData import exceltodict
from search_optimierung import search_words, skip_words
from fuzzywuzzy import fuzz
from collections import defaultdict
from Chefkoch_Scrape import chefkoch_scrape
from Berechnung import calculate_price


### Grundlegende App erstellen
### QUELLE:
### https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
def createApp(secretKey):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretKey
    return app
app = createApp('REZEPTEPREIS')


products = exceltodict() # Lädt alle Produkte aus der Excel-Datei in den Code
selected_products = []  # Liste für ausgewählte Produkte
current_recipe_index = 0  # Index für das aktuelle Proukt im Rezept
recipelist = [] # Gescrapte Rezeptdaten von Chefkoch


### Berechnungseite
### setzt die Suche, das Hinzufügen eines Rezeptes, das Löschen und Hinzufügen einzelner Artikel um
@app.route("/Berechnung", methods=["POST", "GET"])  # Pfade der Webpage
def home():
    
    global selected_products
    global current_recipe_index
    global max_recipe_index
    default_query = ""
    info = ""
    if request.method == 'POST':
        query = request.form.get('query')
        category = request.form.get('category')
        action = request.form.get('action') 
        product_name = request.form.get('product_name') 
        link = request.form.get('console_link') 
        if action == 'weiter':  
            current_recipe_index += 1  # Index für das nächste Rezept erhöhen
        if action == "back":
            current_recipe_index -= 1
    else:
        query = request.args.get('query')
        category = request.args.get('category')
        action = request.args.get('action')
        product_name = request.args.get('product_name')
        link = request.args.get('console_link')  

    if link:
        recipelist.clear()
        selected_products.clear()
        current_recipe_index = 0
        recipelist.append(chefkoch_scrape(link))        
        max_recipe_index = len(recipelist[0][4])
        if(recipelist is not None):
            for original, replacement in search_words:
                query = recipelist[0][4][0][0]
            fuzzy_results = []
            for product in products:
                product_name = product['name'].lower()
                ratio = fuzz.ratio(query, product_name)
                if ratio >= 70:
                    fuzzy_results.append(product)
            normal_results = [product for product in products if query in product['name'].lower()]

            if category:  # Nur nach Kategorie filtern, wenn eine Kategorie angegeben ist
                fuzzy_results = [product for product in fuzzy_results if product['kategorie'] == category]
                normal_results = [product for product in normal_results if product['kategorie'] == category]

            results = fuzzy_results + normal_results
            unique_results = defaultdict(list)
            for product in results:
                unique_results[(product['name'], product['kategorie'])].append(product)
            results = [product for sublist in unique_results.values() for product in sublist]
            results = results[:20]

            if len(results) == 0:
                message = 'Produkt nicht gefunden'
            else:
                message = None
        else:
            if category:  # Nur Produkte der angegebenen Kategorie anzeigen
                results = [product for product in products if product['kategorie'] == category]
            else:
                results = products[:50]
            message = None


    ####### Löschbutton
    ####### Entfernt alle Produkte aus dem Warenkorb und löscht das Rezept        
    if action == "clear":
        recipelist.clear()
        selected_products.clear()

    ##### Setzt die Funktion des "Weiter" Buttons um, damit zum nächsten Artikel in der Rezeptliste gelangt werden kann
    if action == "weiter":
        if(recipelist is not None):
            max_recipe_index = len(recipelist[0][4])
            for original, replacement in search_words:
                if current_recipe_index < len(recipelist[0][4]):
                    query = recipelist[0][4][current_recipe_index][0]
                else:
                    query = ""
            fuzzy_results = []
            for product in products:
                product_name = product['name'].lower()
                ratio = fuzz.ratio(query, product_name)
                if ratio >= 70:
                    fuzzy_results.append(product)
            normal_results = [product for product in products if query in product['name'].lower()]

            if category:  
                fuzzy_results = [product for product in fuzzy_results if product['kategorie'] == category]
                normal_results = [product for product in normal_results if product['kategorie'] == category]

            results = fuzzy_results + normal_results
            unique_results = defaultdict(list)
            for product in results:
                unique_results[(product['name'], product['kategorie'])].append(product)
            results = [product for sublist in unique_results.values() for product in sublist]
            results = results[:20]

            if len(results) == 0:
                message = 'Produkt nicht gefunden'
            else:
                message = None
        else:
            if category:  
                results = [product for product in products if product['kategorie'] == category]
            else:
                results = products[:50]
            message = None 
       
    
    ##### Setzt die Funktion des "Zurück" Buttons um, damit zum vorherigen Artikel in der Rezeptliste gelangt werden kann
    if action == "back":
        if(current_recipe_index < 0):
            return redirect(url_for('home'))
        else:
            if(recipelist is not None):
                    for original, replacement in search_words:
                        if current_recipe_index < len(recipelist[0][4]):
                            query = recipelist[0][4][current_recipe_index][0]
                        else:
                            query = ""
                    fuzzy_results = []
                    for product in products:
                        product_name = product['name'].lower()
                        ratio = fuzz.ratio(query, product_name)
                        if ratio >= 70:
                            fuzzy_results.append(product)
                    normal_results = [product for product in products if query in product['name'].lower()]

                    if category:  
                        fuzzy_results = [product for product in fuzzy_results if product['kategorie'] == category]
                        normal_results = [product for product in normal_results if product['kategorie'] == category]

                    results = fuzzy_results + normal_results
                    unique_results = defaultdict(list)
                    for product in results:
                        unique_results[(product['name'], product['kategorie'])].append(product)
                    results = [product for sublist in unique_results.values() for product in sublist]
                    results = results[:20]

                    if len(results) == 0:
                        message = 'Produkt nicht gefunden'
                    else:
                        message = None
            else:
                if category:  
                    results = [product for product in products if product['kategorie'] == category]
                else:
                    results = products[:50]
                message = None 






    #### Setzt die Suche nach Artikel um (wird für einzel Produktsuche und der Suche nach Artikeln in der Rezeptliste bentutzt)
    if query:
        if ' ' in query:
            query_words = query.split()  
            results = []  
            default_query = query
            for word in query_words:
                replaced_word = word.lower()  
                
                if word.isdigit():
                    continue

                if replaced_word in skip_words:
                    continue

                for original, replacement in search_words:
                    if word.lower() == original.lower():  # Überprüfe, ob das Wort ersetzt werden muss
                        replaced_word = replacement.lower()
                        break
                
                fuzzy_results = []
                for product in products:
                    product_name = product['name'].lower()
                    ratio = fuzz.ratio(replaced_word, product_name)
                    if ratio >= 60:
                        fuzzy_results.append(product)
                
                normal_results = [product for product in products if replaced_word in product['name'].lower()]

                if category:
                    fuzzy_results = [product for product in fuzzy_results if product['kategorie'] == category]
                    normal_results = [product for product in normal_results if product['kategorie'] == category]

                results.extend(fuzzy_results + normal_results)
            
            # Entferne Duplikate aus den Ergebnissen
            unique_results = defaultdict(list)
            for product in results:
                unique_results[(product['name'], product['kategorie'])].append(product)
            results = [product for sublist in unique_results.values() for product in sublist]
            results = results[:600]

            if len(results) == 0:
                message = 'Produkt nicht gefunden'
            else:
                message = None
        else:
            for original, replacement in search_words:
                query = query.lower().replace(original.lower(), replacement.lower())
                default_query = query
            fuzzy_results = []
            for product in products:
                product_name = product['name'].lower()
                ratio = fuzz.ratio(query, product_name)
                if ratio >= 80:
                    fuzzy_results.append(product)
            normal_results = [product for product in products if query in product['name'].lower()]

            if category: 
                fuzzy_results = [product for product in fuzzy_results if product['kategorie'] == category]
                normal_results = [product for product in normal_results if product['kategorie'] == category]

            results = fuzzy_results + normal_results
            unique_results = defaultdict(list)
            for product in results:
                unique_results[(product['name'], product['kategorie'])].append(product)
            results = [product for sublist in unique_results.values() for product in sublist]
            results = results[:50]

            if len(results) == 0:
                message = 'Produkt nicht gefunden'
            else:
                message = None
    else:
        if category: 
            results = [product for product in products if product['kategorie'] == category]
        else:
            results = products[:500]
        message = None

    #### Setzt die Funktion für das Hinzufügene eines Artikels in den Warenkorb um
    if action == 'add':  
        selected_product = next((product for product in products if product['name'] == product_name), None) 
        if(recipelist):
            if(recipelist[0][4][current_recipe_index][2].lower() == "x"):
                info = "Das eingetragen Rezept enthält Zutaten mit ungenauen Mengenangaben. Der Preis kann nicht genau berechnet werden"
                data = {
                    "name": selected_product["name"],
                    "price": selected_product["price"],
                    "menge": selected_product["menge"],
                    "einheit": selected_product["einheit"],
                    "icon": selected_product["icon"],
                    "kategorie": selected_product["kategorie"]
                }
                selected_products.append(data)
            else: 
                total_price = calculate_price(recipelist[0][4][current_recipe_index], selected_product)
                if(total_price == None):
                    total_price = selected_product["price"]
                else:
                    total_price = round(total_price[0],3)
                data = {
                    "name": selected_product["name"],
                    "price": total_price,
                    "menge": recipelist[0][4][current_recipe_index][1],
                    "einheit": recipelist[0][4][current_recipe_index][2],
                    "icon": selected_product["icon"],
                    "kategorie": selected_product["kategorie"]
                }
                selected_products.append(data)
        else: 
            if selected_product:
                info = ""
                print(selected_product)
                selected_products.append(selected_product)
    elif action == 'remove': 
        selected_products = [product for product in selected_products if product['name'] != product_name]
    
    #### Gesamtpreis des Warenkorbs berechnen
    total_price = round(sum(product['price'] for product in selected_products),2) 

    if current_recipe_index < len(recipelist):
        if(current_recipe_index < 0):
            current_recipe_index = 0
            max_recipe_index = len(recipelist[0][4])
        else: 
            current_recipe = recipelist[current_recipe_index]
            max_recipe_index = len(recipelist[0][4])
    else:
        if(len(recipelist) > 0):
            max_recipe_index = len(recipelist[0][4])
            current_recipe = None
        else: 
            current_recipe = None
            max_recipe_index = None
    return render_template('suche.html', info=info, query=query, products=results, default_query=default_query, selected_products=selected_products, total_price=total_price, message=message, recipelist=recipelist, current_recipe=current_recipe, current_recipe_index=current_recipe_index, max_recipe_index=max_recipe_index)

#### Home Seite - zeigt das Video - sonst keine Funktionen
@app.route("/")
def home3():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True) 