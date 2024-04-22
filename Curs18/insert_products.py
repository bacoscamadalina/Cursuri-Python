import sqlite3

conn = sqlite3.connect('marketplace.db')
cursor = conn.cursor()

products_data = [
    ('Smartphone', 'TechCorp', 999.99, 150, 'Smartphone de ultimă generație cu cameră de înaltă calitate'),
    ('Laptop', 'ComputeInc', 1200.00, 75, 'Laptop puternic și portabil, ideal pentru profesioniști'),
    ('Headphones', 'SoundGood', 150.50, 200, 'Căști over-ear cu anulare a zgomotului'),
    ('Smart Watch', 'TechCorp', 299.99, 120, 'Ceas inteligent cu monitorizare a sănătății'),
    ('E-reader', 'ReadWorld', 180.00, 80, 'Dispozitiv de citit electronic cu ecran E-ink'),
    ('Tablet', 'ComputeInc', 450.00, 100, 'Tabletă versatilă cu ecran tactil de 10 inch'),
    ('Wireless Charger', 'TechCorp', 59.99, 300, 'Încărcător wireless rapid și eficient'),
    ('Bluetooth Speaker', 'SoundGood', 99.99, 250, 'Difuzor portabil cu conectivitate Bluetooth'),
    ('External Hard Drive', 'StoragePlus', 200.00, 60, 'Hard disk extern de 1TB pentru stocare suplimentară'),
    ( 'Digital Camera', 'FotoSnap', 500.00, 40, 'Cameră digitală DSLR pentru amatori și profesioniști'),
]   # variabila care ne tine datele pe care vrem sa le inseram

querry = 'INSERT INTO Products(name, category, price, stock_count, description) VALUES (?,?,?,?,?)' # asociaza numele
# cu ?, categoria cu ? si etc. Nu mai trebuie sa scrie valoarea pt fiecare


cursor.executemany(querry,products_data)  # pt ca avem mai multe randuri de inserat
conn.commit()
conn.close()  # ca sa inchidem conexiunea (motiv de securitate)