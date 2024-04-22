import sqlite3

# Crearea conexiunii

conn = sqlite3.connect('marketplace.db')  # conexiune (connection)
cursor = conn.cursor()  # cursor = trimitem date

# creare tabele - var1
creare_tabela_users = ''' 
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
address TEXT,
city TEXT,
postal_code TEXT,
country TEXT);
'''
# primary key = cheia primara dintr-o tabela

creare_tabela_products = '''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name  TEXT NOT NULL,
category TEXT NOT NULL,
price REAL NOT NULL,
stock_count INTEGER DEFAULT 1,
description TEXT);
'''

creare_tabela_orders = '''
CREATE TABLE IF NOT EXISTS Orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER NOT NULL,
order_date TEXT);
'''

creare_tabela_orderitems = '''
CREATE TABLE IF NOT EXISTS Order_Items(
id INTEGER PRIMARY KEY AUTOINCREMENT,
order_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
quantity INTEGER DEFAULT 0,
total_price REAL NOT NULL);
'''

cursor.executescript(creare_tabela_users)
cursor.executescript(creare_tabela_products)
cursor.executescript(creare_tabela_orders)
cursor.executescript(creare_tabela_orderitems)

#intram in SQLigth -> database -> Add