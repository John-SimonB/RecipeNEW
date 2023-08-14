#### Die folgende Funktion rechnet Mengeneinheiten um.
#### Dafür werden die Faktoren zum Rechnung definiert (conversion_facotrs)
#### Liegt die Einheit gültige Einheit vor, wird dies zurückgegeben
#### PARAMETER:
#### quantity = Menge
#### from_unit = Einheit von der aus umgerechnet werden soll
#### to_unit = Einheit in die umgrechent werden soll
#### RETURN:
#### converted_quantity = Umgerechnete Menge
def convert_quantity(quantity, from_unit, to_unit):
    conversion_factors = {
        'g': {
            'kg': 0.001,
            'ml': None  # Keine direkte Umrechnung möglich
        },
        'kg': {
            'g': 1000,
            'ml': None  # Keine direkte Umrechnung möglich
        },
        'l': {
            'ml': 1000,
            'g': None  # Keine direkte Umrechnung möglich
        },
        'ml': {
            'l': 0.001,
            'g': None  # Keine direkte Umrechnung möglich
        },
        'TL': {
            'g': 5,
            'kg': 0.005,
            'ml': 5,  
            'l': 0.005
        },
        'EL': {
            'g': 13,
            'kg': 0.013,
            'ml': 15,  
            'l': 0.015
        },
        'X': {
            'g': None,
            'kg': None,
            'ml': None,  
            'l': None
        },
        'Stk': {
            'g': None,
            'kg': None,
            'ml': None,  
            'l': None,
            'St': 1,
        },
        'St': {
            'g': None,
            'kg': None,
            'ml': None,  
            'l': None,
            'Stk': 1,
        },
    }

    if from_unit == to_unit:
        return quantity, True  # Gleiche Einheit

    conversion_factor = conversion_factors.get(from_unit, {}).get(to_unit)

    if conversion_factor is None:
        return None, False  # Keine gültige Umrechnung möglich

    converted_quantity = quantity * conversion_factor
    return converted_quantity, False


# Daten für Beispielaufruf:
artikel_aus_rezept = ['Weizenmehl Type 405', '0.5', 'Stk']

datenbank_fuer_berechnung = {
    'name': 'Rewe Beste Wahl Weizenmehl Type 405 1kg',
    'price': 1.00,
    'menge': '1',
    'einheit': 'St',
    'icon': 'https://res.cloudinary.com/goflink/image/upload/w_600,h_800/product-images-prod/9a8bf872-ac62-48dc-a0a4-c9672dc37ecb.png',
    'kategorie': 'dauerguenstig'
}

#### Die folgende Funktion berechnet den Preis, dabei wird mit der Prüfung der Mengeneinheiten angefangen.
#### Liegen unterschiedliche Einheiten vor, wird versucht die Einheit zu konvertieren. 
#### Nachdem erfogreichen konvertieren wird der "price_per_unit" ausgrechnet, mitdem anschließend der Preis der benötigten Menge berechnet wird
#### Ist die Umrechnung nicht möglich, dann wird der Vollpreis des Artikels hinterlegt.
#### PARAMETER:
#### recipe_article = zu berechnendes Produkt aus dem Rezept
#### "database_article" = Ausgewähltes Produkt aus der Datenbank
#### RETURN:
#### total_price = ausgerechnetet mengenbezogender Preis
#### message = Meldung über die Beschaffenheit der Einheiten
def calculate_price(recipe_article, database_article):
    if(recipe_article[2] == "Stk" or recipe_article[2] == "St"):
        if(database_article["einheit"] == "Stk" or database_article["einheit"] == "St"):
            price_per_unit = database_article["price"] / float(database_article["menge"])
            total_price = float(recipe_article[1]) * price_per_unit 
            message = "gleiche Einheit (Stk)"
            return total_price, message
        else:
            total_price = database_article["price"]
    else:
        converted_quantity = convert_quantity(float(recipe_article[1]), recipe_article[2], database_article["einheit"])
        if(converted_quantity[1] == True):
            price_per_unit = database_article["price"] / float(database_article["menge"])
            total_price = float(recipe_article[1]) * price_per_unit
            message = "gleiche Einheit"
            return total_price, message
        elif(converted_quantity[0] == None and converted_quantity[1] == False):
            total_price = database_article["price"]
            message = "Einheit nicht gefunden, oder Umrechnung nicht möglich"
            return total_price, message
        else:
            price_per_unit = database_article["price"] / float(database_article["menge"])
            total_price = converted_quantity[0] * price_per_unit
            message = "verschiedene Einheien"
            return total_price, message


# Beispielaufruf:        
#calculate_price(artikel_aus_rezept, datenbank_fuer_berechnung)
