# course_json.py

import json


#dict: 
data = {
    'jméno': 'Anna',
    'město': 'Brno',
    'jazyky': ['čeština', 'angličtina'],
    'věk': 26,
}

kod = json.dumps(data, ensure_ascii=False, indent=2)
print(kod)
# writing to the file.json
""" 
with open('data.json', 'w') as soubor: 
    print(kod, file=soubor)
""" 

# reading the file.json
with open('data.json') as soubor: 
    kod = soubor.read()
print()


# transform back to dict and working with it: 
data = json.loads(kod)
print(data)

