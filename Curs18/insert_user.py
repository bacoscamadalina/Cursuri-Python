import sqlite3
from pprint import pprint

# Crearea conexiunii

conn = sqlite3.connect('marketplace.db')  # conexiune (connection)
cursor = conn.cursor()  # cursor = trimitem date

cursor.execute('''
INSERT INTO Users (username, email, password, first_name, last_name, address, city, postal_code, country)
Values('john_doe', 'john.doe@example.com', 'JDoe#2022', 'John', 'Doe', '123 Maple Street', 'Springfield', '12345', 'USA');
''')

cursor.execute("""
INSERT INTO Users(username, email, password, first_name, last_name, address, city, postal_code, country)
Values('jane_smith', 'jane.smith@example.net', 'JSmith#2022', 'Jane', 'Smith', '456 Oak Avenue', 'Centerville', '67890', 'Canada');
""")  # cu aceasta comanda inseram valori in baza de date

# conn.commit()   # se executa pt a putea afisa(salva) valorile in baza de Date -> nu il punem daca vrem sa tesstam

cursor.execute('select * from users;')  # query de a selecta toate coloanele (* = tot) din tabela users
pprint(cursor.fetchall())  # fetchall - le ia (citeste) pe toate, fetchone - ia doar una, fetchmany(punem nr)