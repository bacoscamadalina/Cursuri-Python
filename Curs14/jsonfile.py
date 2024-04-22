'''
JSON FILE

{
    "studenti": [
        {
            "nume": "Ion Popescu",
            "varsta": 22,
            "cursuri": ["Matematică", "Fizică", "Informatică"],
            "absolvent": false,
            "contact": {
                "email": "ion.popescu@example.com",
                "telefon": "0712345678"
            }
        },
        {
            "nume": "Maria Ionescu",
            "varsta": 21,
            "cursuri": ["Literatură", "Istorie", "Arte"],
            "absolvent": false,
            "contact": {
                "email": "maria.ionescu@example.com",
                "telefon": "0723456789"
            }
        }
    ]
}

'''

import json
from pprint import pprint


def read(filename):
    with open(filename, 'r') as f:
       return json.load(f)


print(read('studenti.json'))


def write(filename,data):
    with open(filename,'w') as f:
        json.dump(data,f,indent =4)


data ={
    "indivizi": [
        {"nume": "Ana Popescu", "varsta": 28, "ocupatie": "Inginer software", "oras": "Cluj-Napoca"},
        {"nume": "Bogdan Ionescu", "varsta": 34, "ocupatie": "Manager Proiect", "oras": "București"},
        {"nume": "Cristina Enache", "varsta": 25, "ocupatie": "Designer Grafic", "oras": "Iași"},
        {"nume": "Dorin Georgescu", "varsta": 30, "ocupatie": "Analist Financiar", "oras": "Timișoara"}
    ]
}

write('indivizi.json',data)


def append(filename,data):
    with open(filename,'a') as f:
        json.dump(data,f,indent = 2)


append('indivizi.json',data)