'''
1.Write a SQL statement that groups all countries by continents, and counts them.
2.Write a SQL statement that groups all countries by continent, and computes the total population per continent (SUM).
'''

# Exercitiul 1
print('EX1')
import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

group_by_continents = '''
    SELECT COUNT(*) as numar_tari, continents.Continent_name FROM Countries JOIN continents ON continents.continent_id = Countries.continent_id GROUP BY Countries.continent_id;
'''

cursor.execute(group_by_continents)
pprint(cursor.fetchall())
