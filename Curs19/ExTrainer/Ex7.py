'''
Write a SQL statement to select only countries that start with a certain letter (choose one that exists for you, e.g.
C in the example above)
'''
import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

select_certain_letter = '''
    SELECT * FROM Countries WHERE country_name LIKE '%SS%'
'''

# C% orice incepe cu litera C, %A orice se termina cu litera C , %SS% orice are in mijloc SS
cursor.execute(select_certain_letter)
pprint(cursor.fetchall())


# '____' gasim orice cuvant din 4 litere
wild_card = '''
    SELECT * FROM Countries WHERE country_name LIKE  '_ND%'
'''
cursor.execute(wild_card)
pprint(cursor.fetchall())