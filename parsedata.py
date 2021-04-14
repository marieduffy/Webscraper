import json

with open('jobData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print(i["title_elem"])