'''
Write a SQL statement to select only countries with a population greater than 20 millions.
'''

import sqlite3
from pprint import pprint

from Curs19.ExTrainer import constants
import csv

conn = sqlite3.connect(constants.DATABASE)
cursor = conn.cursor()

select_over_twenty= '''
    SELECT * FROM Countries WHERE population>20;
'''
cursor.execute(select_over_twenty)
pprint(cursor.fetchall())