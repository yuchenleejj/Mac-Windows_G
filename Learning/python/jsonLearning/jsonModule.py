import json
# The reason I learn this module is to deal with my notion api project
# test git 

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@gmail.com", " johnsmith@yahoo.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data))
print(data['people'])
print(data['people'][0])
print(data['people'][0]['name'])
print(data['people'][0]['phone'])
print(data['people'][0]['emails'])
print(data['people'][0]['emails'][0])
print(data['people'][0]['has_license'])

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

# Path: Learning\python\json\jsonModule2.py
import json

with open('people.json') as f:
    data = json.load(f)

for person in data['people']:
    print(person['name'])
    del person['area_codes']
    
with open('new_people.json', 'w') as f:
    json.dump(data, f, indent=4)

# Path: Learning\python\json\jsonModule3.py
import json
from urllib.request import urlopen

with urlopen('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json') as response:
    source = response.read()

data = json.loads(source)
print(json.dumps(data,indent=2))
