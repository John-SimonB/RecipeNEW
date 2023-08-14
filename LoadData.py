import pandas as pd

#### Lädt die Daten aus der Exceldatei in den Code
#### QUELLE:
#### https://stackoverflow.com/questions/43964513/importing-an-excel-file-to-python
#### https://datatofish.com/read_excel/
def exceltodict():
  df = pd.read_excel('Data.xlsx')
  data = []
  for index, row in df.iterrows():
    item = {
      "name" : row["name"],
      "price" : row['price'],
      "menge" : row['menge'],
      "einheit" : row['einheit'],
      "icon" : row['icon'],
      "kategorie" : row["kategorie"]
      }
    data.append(item)
  return data

data = exceltodict()


