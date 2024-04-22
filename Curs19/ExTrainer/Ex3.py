'''
Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
'''

import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()



script = '''
    CREATE TABLE IF NOT EXISTS Countries (
    country_code CHAR(2) PRIMARY KEY,
    country_name TEXT,
    continent_id INTEGER,
    population INTEGER,
    FOREIGN KEY (continent_id) REFERENCES continents(continent_id)
    );
'''

cursor.execute(script)
conn.commit()
conn.close()