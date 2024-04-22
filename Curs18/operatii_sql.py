import sqlite3
from pprint import pprint

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()


# modificam un produs
def update_product_price(product_id, new_price):
    cursor.execute('UPDATE Products SET price = ? WHERE id = ?', [new_price, product_id])
    conn.commit()  # nu dam commit pana nu suntem siguri, deoarece nu mai putem modifica inapoi datele


update_product_price(1, 1000)

# stergerea unui produs
def delete_product_byid(product_id):
    cursor.execute('DELETE FROM Products WHERE id = ?',[product_id])
    conn.commit()

delete_product_byid(7)

# select
def get_prod_by_category(category):
    cursor.execute('SELECT * FROM Products WHERE category = ?', [category])
    product = cursor.fetchall()
    pprint(product)
    conn.commit()

get_prod_by_category('TechCorp')

# cea mai buna, complexa baza de date este "PLSQL"
# rollback - sterge ultimul commit
