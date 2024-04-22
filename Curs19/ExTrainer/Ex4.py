'''
Write a few SQL statements to add some countries. Here is a list of countries with their codes.
Feel free to invent or approximate their populations, and use your geography knowledge for their continent.
Add at least 10 countries, as diverse as possible (INSERT). Examples:
– Romania, EU, 19mil
– USA, NA, 330mil
– France, EU, 70mil
– Hungary, EU,  9mil
– Canada, NA, 40mil
– China, AS, 1450mil
– Belgium, EU, 12mil
–  Egypt, AF, 110mil
– Australia, OC, 25mi
'''

import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants
import csv

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()
insert_countries = []
with open('countries.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        row[-1] = row[-1].replace('mil', ' ')
        print(row)
        insert_countries.append(row)
print(insert_countries)

script = '''
    INSERT INTO Countries(country_name,country_code,continent_id,population)
    VALUES (?,?,?,?)
'''

cursor.executemany(script, insert_countries)
conn.commit()
conn.close()
