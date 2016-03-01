import csv
import json

csvpath = "./data/datause1filtered.csv"
jsonpath = "./data/datause1filtered.json"

jsonData=[]
headers=[
 "censusTract",
 "Change_Population",
 "Change_HouseUnits",
 "Change_5To7_or_more_person_household",
 "Change_Builst1939earlier",
 "Change_Built_1940to1959",
 "Change_VacantUnits",
 "Y00_PCT_Units_HHIncome_25to50k",
 "Y00_PCT_Units_HHIncome_50to75k",
 "Chg_Educate_HighSchool_orLess",
 "Chg_Educate_SomeCollege",
]

with open(csvpath,'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    tempRow = []
    tractId = row[2]
    tractId = tractId[9:20]
    if tractId.isdigit():
      tempRow.append(tractId)
      for x in range(4,14):
        tempRow.append(row[x])

      tempJson = {}
      for x in range(len(tempRow)):
        tempJson[headers[x]] = tempRow[x]
      json.dumps(tempJson)
      jsonData.append(tempJson)

with open(jsonpath, 'w') as jsonfile:
  json.dump(jsonData,jsonfile)

