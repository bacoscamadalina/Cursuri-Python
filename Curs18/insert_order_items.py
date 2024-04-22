import sqlite3

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

order_items_data = [
    (1, 1, 2, 1999.98),
    (1, 3, 1, 150.50),
    (2, 2, 1, 1200.00),
    (2, 4, 1, 299.99),
    (3, 5, 3, 540.00),
    (3, 7, 2, 119.98),
    (4, 6, 1, 450.00),
    (4, 8, 1, 99.99),
    (5, 9, 1, 200.00),
    (5, 10, 1, 500.00),
    (6, 1, 1, 999.99),
    (6, 2, 2, 2400.00),
    (7, 3, 3, 451.50),
    (7, 4, 2, 599.98),
    (8, 5, 2, 360.00),
    (8, 7, 1, 59.99),
    (9, 6, 1, 450.00),
    (9, 8, 2, 199.98),
    (10, 9, 2, 400.00),
    (10, 10, 1, 500.00),
]   # variabila care ne tine datele pe care vrem sa le inseram

querry = 'INSERT INTO Order_Items (order_id, product_id, quantity, total_price) Values (?, ?, ?, ?)' # asociaza numele
# cu ?, categoria cu ? si etc. Nu mai trebuie sa scrie valoarea pt fiecare


cursor.executemany(querry,order_items_data)  # pt ca avem mai multe randuri de inserat
conn.commit()
conn.close()  # ca sa inchidem conexiunea (motiv de securitate)