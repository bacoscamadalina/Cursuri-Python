'''
Write a SQL statement to select all countries, ordered by name. Write another statement to count them all.
'''
import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants
import csv

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

select_all_countries = '''
    SELECT * FROM Countries ORDER BY country_name DESC;
'''

# vedem cate linii avem intr-o tabela
count_all_country = '''
    SELECT  COUNT(*) FROM Countries; 
'''

cursor.execute(select_all_countries)
pprint(cursor.fetchall())  # ca sa ne dea toate rezultatele

cursor.execute(count_all_country)
pprint(cursor.fetchone())