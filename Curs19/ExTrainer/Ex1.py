'''
1. Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code, use this link
'''

import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

script = '''
    CREATE TABLE IF NOT EXISTS continents(
    Continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Continent_name TEXT,
    Continent_code CHAR(2));
'''

cursor.execute(script)
conn.commit()
conn.close()