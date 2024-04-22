import sqlite3

conn = sqlite3.connect("my_database.db")
conn.execute('''
    CREATE TABLE IF NOT EXISTS istoric (
        id INTEGER PRIMARY KEY,
        nume TEXT NOT NULL,
        varsta INTEGER NOT NULL
    );
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS persoane (
        id INTEGER PRIMARY KEY,
        nume TEXT NOT NULL,
        varsta INTEGER NOT NULL
    );
''')

persoane = [
    ("Alice", 25),
    ("Bob", 30),
    ("Carol", 22),
    ("David", 28),
    ("Eve", 35)
]

for p in persoane:
    conn.execute("INSERT INTO persoane (nume, varsta) VALUES (?, ?)", p)

# in mom in care se sterge un entry din tabela, inainte de comanda delete el va face un insert, inainte sa stearga din
# persoana are un begin si un end. Se pune .old deaorece ceea ce s-a sters se va insera in tabela (inserezi ceea ce s-a sters)

# TRIGGER = Ne salveaza automat ceva sters dintr-un tabel, in altul (intr-un istoric de tabel)

conn.execute('''
    CREATE TRIGGER IF NOT EXISTS before_delete_history
    BEFORE DELETE ON persoane
    BEGIN
        INSERT INTO istoric (id, nume, varsta)
        SELECT OLD.id, OLD.nume, OLD.varsta;
    END;
''')

conn.commit()
conn.close()

print("Baza de date a fost actualizată cu succes!")
