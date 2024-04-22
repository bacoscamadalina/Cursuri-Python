import sqlite3

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

orders_data = [
    (1, 101, '2022-09-01'),
    (2, 102, '2022-09-02'),
    (3, 103, '2022-09-03'),
    (4, 104, '2022-09-04'),
    (5, 105, '2022-09-05'),
    (6, 106, '2022-09-06'),
    (7, 107, '2022-09-07'),
    (8, 108, '2022-09-08'),
    (9, 109, '2022-09-09'),
    (10, 110, '2022-09-10'),
]   # variabila care ne tine datele pe care vrem sa le inseram

querry = 'INSERT INTO Orders (id, customer_id, order_date) Values (?, ?, ?)' # asociaza numele
# cu ?, categoria cu ? si etc. Nu mai trebuie sa scrie valoarea pt fiecare


cursor.executemany(querry,orders_data)  # pt ca avem mai multe randuri de inserat
conn.commit()
conn.close()  # ca sa inchidem conexiunea (motiv de securitate)