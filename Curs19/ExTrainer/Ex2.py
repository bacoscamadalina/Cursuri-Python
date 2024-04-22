'''
Using the link above, write all SQL statements needed to add all the seven continents (INSERT).
'''


import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

continents = ''' Asia AS, Africa AF, North_America NA, South_America SA, Antarctica AN, Europe EU, Australia AU'''
insert_continents = []

for c in continents.split(','):   # face delimitare
    #    print(c.split())
    continent_name, continent_code = c.split()
    insert_continents.append((continent_name,continent_code))

print(insert_continents)

script = '''
    INSERT INTO Continents(continent_name,continent_code)
    VALUES(?,?)
'''

cursor.executemany(script,insert_continents)
conn.commit()
conn.close()