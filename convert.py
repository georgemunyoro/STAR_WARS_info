import csv
import json

csvFilePath = "./data/vehicles.csv"
jsonfilepath = "./data/vehicles.json"

data = {}
count = 0
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = count
        data[id] = rows
        count += 1

print(data)

with open(jsonfilepath, "w") as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
