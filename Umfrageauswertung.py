import pandas as pd

### Wurde teilweise für die Auswertung der Umfrage benutzt. 
### ist nicht relevant für die Webseite.



def loadData():
    excel_file_path = "Umfrage.xlsx"
    try:
        df = pd.read_excel(excel_file_path)
        print("Excel-Tabelle erfolgreich eingelesen.")
        Persons = []

        for index, row in df.iterrows():
            person = {
                "geschlecht": row["Mit welchem Geschlecht identifizieren Sie sich?"],
                "alter" : row["Zu welcher Altersgruppe gehören Sie?"],
                "angestellt": row["Wie ist Ihr aktuelles Beschäftigungsverhältnis? (Angestelle/r)"],
                "verhältnis": row["In welcher Anstellungsart befinden Sie sich? (Teilzeit (auch Werkstudent/in))"],
                "einkommen" : row["Wie hoch ist Ihr durchschnittliches monatliches Nettoeinkommen?"],
                "kochen" : row["Wie oft kochen Sie selbst?"],
                "bockaufapp" : row["Wären Sie daran interessiert, eine webbasierte Anwendung zur automatisierten Berechnung von Preisen und Mengen für Chefkoch-Rezepte zu nutzen?"],
                "kalkulieren_versuch" : row["Versuchen Sie die Preise für ein gewähltes Rezept vor dem Einkauf zu kalkulieren?"],
                "kalkulieren_würden" : row["Würden Sie gern Preise für ein gewähltes Rezept vor dem Einkauf kalkulieren?"],
                "rezepte_ohne_preis":   [row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Spargel-Brotsalat - Zutaten: Ciabatta, Knoblauchzehe, grüner Spargel, Kirschtomaten, Basilikum, Rotweinessig, Olivenöl, Parmesan)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Cremiger Nudelauflauf mit Tomaten und Mozzarella - Zutaten: Zwiebel, Knoblauch, Chilischote, Cherrytomaten, Parmesan, Mozzarella, Basilikum, Rigatoni oder Penne, Olivenöl, passierte Tomaten, Sahne)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Nudelsalat - Zutaten: Spinelli, Erbsen TK, Fleischwurst oder Wiener, Gouda oder Ementaler, Tomaten, Gewürzgurken, Salatcreme, Ketchup, Senf)"],
                                        row ["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Hackbraten auf italienische Art - Zutaten: Hackfleisch, Brötchen, Zwiebel, Ei, Basilikum, Oliven schwarz ohne Stein, getrocknete Tomaten, Knoblauch, Mozzarella, Parmaschinken)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Hähnchen Ananas Curry mit Reis - Zutaten: Hähnchen, Ananas, Sahne, Schmelzkäse, Lauchzwiebel, Knoblauch, Honig, Curry, Reis)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Zitronenkuchen - Zutaten: Margarine, Mehl, Zucker, Vanillezucker, Backpulver, Ei, Zitronen, Puderzucker)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Panzanella mit Bohnen Rucola und Vinaigrette - Zutaten: Knoblauch, Olivenöl, Mazzetii Condimento Bianco, Ciabatta, rote Zwiebel, Rocula, weiße Bohnen)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Lachs Sahne Gratin - Zutaten: Sahne, Lachs, Gemüsebrühe, Pfeffer, Dill, Speisestärke, Tomatenmark, Knoblauch, Schalotten, Fett)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Fantakuchen mit Mandarinen-Schmand - Zutaten: Ei, Zucker, Vanillezucker, Mehl, Backpulver, Öl, Fanta, Mandarinen, Schlagsahne, Sahnesteif, Schmand)"],
                                        row["Ihnen werden nun unterschiedliche Gerichte angezeigt, kreuzen Sie an welche/s Sie gern kochen würden. (Bulgur, Buddha Bowl - Zutaten: Bulgur, Avocados, Champignons, Paprika, Zwiebel, Tomate, Hummus, Kichererbsen, Gurke, Geta-Käse, Lauchzwiebel, Tomatenmark, Zitronensaft, Petersilie, Balsamico, Olivenöl)"]],
                "rezepte_mit_preis":    [row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Spargel Brotsalat: 4 Portionen 18,69€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Cremiger Nudelauflauf mit Tomaten und Mozzarella: 4 Portionen 21,15€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Nudelsalat: 4 Portionen 14,34€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Hackbraten auf italienische Art: 4 Portionen 20,87€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Hähnchen Ananas Curry mit Reis: 4 Portionen 24,79€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Zitronenkuchen: 1 Blech 10,08€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Panzanella mit Bohnen Rucola und Vinaigrette: 4 Portionen 12,28€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Lachs Sahne Gratin: 4 Portionen 23,32€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Fantakuchen mit Mandarinen-Schmand; 1 Blech 16,72€)"],
                                        row["Unter Berücksichtigung des Preises, wählen Sie erneut welche/s Gericht Sie kochen würden. Der Rezeptpreis wurde anhand von Flink-Online Preisen ermittelt. (Bulgur Buddha Bowl: 4 Portionen 24,23€)"]]
            }
            Persons.append(person)

        count_from_to = 0
        count_female_from_to = 0
        count_male_from_to = 0
        suche = "über 65 Jahre" # Wert für die Altersgruppe
        for person in Persons:
            if person['alter'] == suche:
                count_from_to += 1
                if person['geschlecht'] == 'Weiblich':
                    count_female_from_to += 1
                else:
                    count_male_from_to += 1
        print("Ergebnisse für: " + suche)
        print("Frau: " + str(count_female_from_to)+ " === " + str((count_female_from_to/51) * 100))
        print("Mann: " + str(count_male_from_to)+ " === " + str((count_male_from_to/51) * 100))
        print("Gesamt: " + str(count_from_to)+ " === " + str((count_from_to/51) * 100))

        ## Einkommen
        einkommen = "1700 - 2299€" # Wert für die Einkommensspanne
        count_euro_angestellt_female = 0
        count_euro_angestellt_male = 0
        count_euro = 0
        for person in Persons:
            if(person["einkommen"] == einkommen):
                    count_euro += 1
                    if person['geschlecht'] == 'Weiblich':
                        count_euro_angestellt_female += 1
                    else:
                        count_euro_angestellt_male += 1
        print("")
        print("Ergebnisse für: " + einkommen + " jede Anstellungsart")
        print("Frau: " + str(count_euro_angestellt_female) + " === " + str((count_euro_angestellt_female/51) * 100))
        print("Mann: " + str(count_euro_angestellt_male) + " === " + str((count_euro_angestellt_male/51) * 100))
        print("Gesamt: " + str(count_euro)+ " === " + str((count_euro/51) * 100))

        ## Kochen
        count_kochen_female = 0
        count_kochen_male = 0
        count_kochen = 0
        kochen = "Siebenmal pro Woche" # Wert für die Häufigkeit des Kochens
        for person in Persons:
            if(person["kochen"] == kochen):
                    count_kochen += 1
                    if person['geschlecht'] == 'Weiblich':
                        count_kochen_female += 1
                    else:
                        count_kochen_male += 1
        print("")
        print("Ergebnisse für: " + kochen )
        print("Frau: " + str(count_kochen_female) + " === " + str((count_kochen_female/51) * 100))
        print("Mann: " + str(count_kochen_male) + " === " + str((count_kochen_male/51) * 100))
        print("Gesamt: " + str(count_kochen)+ " === " + str((count_kochen/51) * 100))
        


        ## Kalkulieren sie bereits ?
        count_kalk = 0
        results = []
        count_below_600 = 0
        count_600_999 = 0
        count_1000_1699 = 0
        count_1700_2299 = 0
        count_2300_3000 = 0
        count_over_3000 = 0
        for person in Persons:
            if(person["kalkulieren_versuch"] == "Ja"):
                results.append(person)
                count_kalk += 1

        for person in results:
            if person['einkommen'] == 'unter 600€':
                count_below_600 += 1 
            if person['einkommen'] == '600 - 999€':
                count_600_999 += 1 
            if person['einkommen'] == '1000 - 1699€':
                count_1000_1699 += 1    
            if person['einkommen'] == '1700 - 2299€':
                count_1700_2299 += 1
            if person['einkommen'] == '2300 - 3000€':
                count_2300_3000 += 1
            if person['einkommen'] == 'über 3000€':
                count_over_3000 += 1
        print("")
        print("Ergebnisse für: Vor dem Einkauf kalkulieren")
        print("unter 600€: " + str(count_below_600) + " === " + str((count_below_600/51) * 100))
        print("zwischen 600 - 999€: " + str(count_600_999)+ " === " + str((count_600_999/51) * 100))
        print("zwischen 1000 - 1699€: " + str(count_1000_1699)+ " === " + str((count_1000_1699/51) * 100))
        print("zwischen 1700 - 2299€: " + str(count_1700_2299)+ " === " + str((count_1700_2299/51) * 100))
        print("zwischen 2300 - 3009€: " + str(count_2300_3000)+ " === " + str((count_2300_3000/51) * 100))
        print("über 3000€: " + str(count_over_3000)+ " === " + str((count_over_3000/51) * 100))
        print("Gesamt: " + str(count_kalk)+ " === " + str((count_kalk/51) * 100))



    ## Kalkulieren würden sie ?
        count_kalk = 0
        results = []
        count_below_600 = 0
        count_600_999 = 0
        count_1000_1699 = 0
        count_1700_2299 = 0
        count_2300_3000 = 0
        count_over_3000 = 0
        for person in Persons:
            if(person["kalkulieren_würden"] == "Ja"):
                results.append(person)
                count_kalk += 1

        for person in results:
            if person['einkommen'] == 'unter 600€':
                count_below_600 += 1 
            if person['einkommen'] == '600 - 999€':
                count_600_999 += 1 
            if person['einkommen'] == '1000 - 1699€':
                count_1000_1699 += 1    
            if person['einkommen'] == '1700 - 2299€':
                count_1700_2299 += 1
            if person['einkommen'] == '2300 - 3000€':
                count_2300_3000 += 1
            if person['einkommen'] == 'über 3000€':
                count_over_3000 += 1
        print("")
        print("Ergebnisse für: Würden gern vor dem Einkauf kalkulieren")
        print("unter 600€: " + str(count_below_600)+ " === " + str((count_below_600/51) * 100))
        print("zwischen 600 - 999€: " + str(count_600_999)+ " === " + str((count_600_999/51) * 100))
        print("zwischen 1000 - 1699€: " + str(count_1000_1699)+ " === " + str((count_1000_1699/51) * 100))
        print("zwischen 1700 - 2299€: " + str(count_1700_2299)+ " === " + str((count_1700_2299/51) * 100))
        print("zwischen 2300 - 3009€: " + str(count_2300_3000)+ " === " + str((count_2300_3000/51) * 100))
        print("über 3000€: " + str(count_over_3000)+ " === " + str((count_over_3000/51) * 100))
        print("Gesamt: " + str(count_kalk)+ " === " + str((count_kalk/51) * 100))

         # Zähler für Personen, die den Preis kalkulieren würden
        nein_ja_kalkulieren = 0

        # Durchlaufe die gegebene Liste und zähle Personen mit 'kalkulieren_versuch' gleich 'Nein',
        # die den Preis kalkulieren würden ('kalkulieren_würden' gleich 'Ja')
        for person in Persons:
            if person['kalkulieren_versuch'] == 'Nein' and person['kalkulieren_würden'] == 'Ja':
                nein_ja_kalkulieren += 1

        # Ausgabe der Anzahl
        print("Anzahl der Personen, die den Preis kalkulieren würden und 'kalkulieren_versuch' gleich 'Nein' haben: " +str(nein_ja_kalkulieren) + " --- " + str((nein_ja_kalkulieren/51) * 100))



        # Vergleich der Ergebnisse aus Frage 19 und 20
        add_result = 0
        remove_result = 0
        changes_result = 0
        preis_egal = 0
        rezept_unrelevant = 0
        for person in Persons:
            list1 = person['rezepte_ohne_preis']
            list2 = person['rezepte_mit_preis']

            add = 0
            remove = 0
            for i in range(len(list1)):
                    if list1[i] != list2[i]:
                        changes_result += 1
                        if(list1[i] == 0 and list2[i] == 1):
                            add += 1
                            add_result += 1
                        if(list1[i] == 1 and list2[i] == 0):
                            remove += 1
                            remove_result += 1
                    if list1[i] == list2[i]:
                        if(list1[i] == 1 and list2[i] == 1):
                            preis_egal +=1
                        if(list1[i] == 0 and list2[i] == 0):
                            rezept_unrelevant +=1


            # Neu hinzugefügt : 0 - 1
            # Gelöscht: 1 - 0
            # Preis interessiert nicht : 1 - 1
            # Rezept interessiert nicht : 0 - 0


            # Anzahl der entfernten Elemente
            removed_elements = len(list1) - len(list2)
            #print("")
            #print("Anzahl der Veränderungen:", num_changes)
            #print("Hinzufügen neuer Rezepte:", add)
            #print("Löschen der Rezepte:", remove)s
        print("")
        print("Insgesamt neu hinzugefügt wurden:", add_result)
        print("Insgesamt neu gelöscht wurden:",remove_result)
        print("Insgesamte Veränderungen:",changes_result)
        print("Mögliche Änderungen insgesamt: " + str(10*51))
        print("Rezept nicht interessant:", rezept_unrelevant)
        print("Preis egal", preis_egal)
        results_rezepte = []
        for person in Persons:
            bla = [person["rezepte_ohne_preis"], person["rezepte_mit_preis"]]
            results_rezepte.append(bla)
        # Liste, um die Gesamtanzahl der Veränderungen von 0 zu 1 für jeden Eintrag zu speichern
        changes_0_to_1_per_entry = [0] * 10
        # Liste, um die Gesamtanzahl der Veränderungen von 1 zu 0 für jeden Eintrag zu speichern
        changes_1_to_0_per_entry = [0] * 10
        # Liste, um die Anzahl der unveränderten Einträge für jeden Eintrag zu speichern
        changes_1_to_1_per_entry = [0] * 10
        changes_0_to_0_per_entry = [0] * 10
        # Iteriere durch die Daten der Teilnehmer
        for person in results_rezepte:
            list1, list2 = person

            # Iteriere durch die Listen und zähle die Veränderungen für jeden Eintrag separat
            for i in range(len(list1)):
                if list1[i] == 0 and list2[i] == 1:
                    changes_0_to_1_per_entry[i] += 1
                elif list1[i] == 1 and list2[i] == 0:
                    changes_1_to_0_per_entry[i] += 1
                elif list1[i] == 1 and list2[i] == 1:
                    changes_1_to_1_per_entry[i] += 1
                elif list1[i] == 0 and list2[i] == 0:
                    changes_0_to_0_per_entry[i] += 1
            


        # Gebe die Gesamtanzahl der Veränderungen für jeden Eintrag aus
        for i in range(len(changes_0_to_1_per_entry)):
            print("")
            print(f"Eintrag: {i+1} Mögliche Änderung gesamt: {changes_0_to_1_per_entry[i]+changes_1_to_0_per_entry[i]+changes_1_to_1_per_entry[i]+changes_0_to_0_per_entry[i]}")
            print(f"Gesamtanzahl des hinzufügen für Eintrag {i+1}: {changes_0_to_1_per_entry[i]}")
            print(f"Gesamtanzahl des löschen für Eintrag {i+1}: {changes_1_to_0_per_entry[i]}")
            print("Anzahl der nicht veränderten Werte: " + str(51-changes_0_to_1_per_entry[i]-changes_1_to_0_per_entry[i]))
            print(f"Anzahl der Preis egal: {changes_1_to_1_per_entry[i]}")
            print(f"Anzahl der Rezept intessiert mich nicht: {changes_0_to_0_per_entry[i]}")


        print("")
        vorher = []
        nachher = []
        for person in Persons:
            vorher.append(person["rezepte_ohne_preis"])
            nachher.append(person["rezepte_mit_preis"])

        def count_changes(vorher, nachher):
            num_entries = len(vorher[0])
            num_changes = [0] * num_entries

            for v_row, n_row in zip(vorher, nachher):
                for i, (v, n) in enumerate(zip(v_row, n_row)):
                    if v != n:
                        num_changes[i] += 1

            return num_changes

        def compare_results(vorher, nachher):
            num_entries = len(vorher[0])
            count_vorher = [0] * num_entries
            count_nachher = [0] * num_entries

            for v_row in vorher:
                for i, v in enumerate(v_row):
                    if v == 1:
                        count_vorher[i] += 1

            for n_row in nachher:
                for i, n in enumerate(n_row):
                    if n == 1:
                        count_nachher[i] += 1

            return count_vorher, count_nachher

        changes = count_changes(vorher, nachher)
        vorher_counts, nachher_counts = compare_results(vorher, nachher)

        print("Gegenüberstellung der Änderungen:")
        for i in range(len(changes)):
            print(f"Eintrag {i + 1} vorher: {vorher_counts[i]} mal, nachher: {nachher_counts[i]} mal, Änderungen: {changes[i]} mal")


        #unter 16 Jahre
        #16 - 22 Jahre
        #23 - 30 Jahre
        #31 - 50 Jahre
        #51 - 65 Jahre
        #über 65 Jahre

        suche = "über 65 Jahre" # Wert für die Altersgruppe
        count_ja = 0
        count_suche_age = 0
        for person in Persons:
            if(person["bockaufapp"] == "Ja, definitiv" or person["bockaufapp"] == "Ja, wahrscheinlich"):
                count_ja += 1
                if person['alter'] == suche:
                    count_suche_age += 1
        print("")
        print(count_ja)
        print(count_suche_age)


    except FileNotFoundError:
        print(f"Datei {excel_file_path} wurde nicht gefunden.")
    except Exception as e:
        print("Fehler beim Einlesen der Excel-Tabelle:", e)

#loadData()