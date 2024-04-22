'''
LISTELE - sunt o insusire de elemente oridonate
        - pot avea valori diferite
        - putem accesa orice index
        - putem adauga valori repetabile
        - sunt mutabile (putem adauga,sterge si inlocui elemente)
'''

lista_diverse = [2, 3.15, False, 'Elefant', 12345]
print(lista_diverse)
# Accesam elemente (index)
print('Accesam elemente')
element_doi = lista_diverse[1]
print(element_doi)
ultimul_element = lista_diverse[-1]
print(ultimul_element)
# Determinam lungimea
print('Determinam lungimea')
lungime_lista = len(lista_diverse)
print(lungime_lista)

# OPERATII CU ELEMENTE/LISTE

# Adaugarea uni nou element in lista
# OPTIUNEA 1 - la sfarsitul listei cu "append"
print('Adaugare la sfarsitul listei')
lista_diverse.append('Carte')
print(lista_diverse)
# OPTIUNEA 2 - in interiorul listei cu "insert"
print('Adaugare in interiorul listei')
lista_diverse.insert(3, 10 * 10)
print(lista_diverse)

print('Inlocuirea unui element din lista')
# Inlocuirea unui element din lista
lista_diverse[2] = True
print(lista_diverse)

# Stergerea ultimului element din lista
print('Stergerea ultimului element')
lista_diverse.pop()
print(lista_diverse)
# Stergem un element
print('Stergerea unui element oarecare')
lista_diverse.pop(3)
print(lista_diverse)

# Incersarea listei
print('Inversarea listei')
lista_inversa = lista_diverse[::-1]
print(lista_inversa)

# List slicing
print('List slicing')
lst_1 = lista_diverse[:3]  # de la primul index (index) pana la index 3, dar index 3 nu este inclus
print(lst_1)
lst_2 = lista_diverse[3:]  # de la indexul 3 pana la sfarsit, iar indexul 3 va fi inclus (de la el incepe)
print(lst_2)

# List slicing - inversarea ultimelor trei elemente
lst_inv = lista_inversa[-3:]
print(lst_inv)
print(30 * '-')

'''
DICTIONARE - sunt o colectie de date de tip cheie : valoare (fiecare cheie are o valoare)
           - sunt mutabile
           - cheile sunt unice
           - valorile se pot repeta
           - cheile pot fi doar : int, str, tuple 
'''
persoana = {
    'nume': 'Vali',
    'prenume': 'Dan',
    'varsta': 30
}
print(f'Persoana = {persoana}')
# Adaugarea unui element in dictionar
print('Adaugarea unui element in dict')
persoana['Initiala tatalui'] = 'P'
print(f'Persoana = {persoana}')

print('Inlocuirea unui element')
persoana['Initiala tatalui'] = 'L'
print(f'Persoana = {persoana}')

print('Stergem un element')
sters = persoana.pop('Initiala tatalui')
print(f'Persoana = {sters}')
print(persoana)

# Lungimea dictionarului
print('Lungimea dictionarului')
lungime_dict = len(persoana)
print(lungime_dict)

# Combinarea a doua dictionare
print('Combinarea a doua dictionare')
d1 = {
    'a': 1,
    'b': 2
}
d2 = {
    'c': 3,
    'd': 4
}
print(d2)
d1.update(d2)
print(d1)

# Stergerea  cheilor si valorilor din dictionar
print('Stergerea cheilor si valorilor din dict')
d1.clear()
print(d1)

'''
SETURI - o colectie de elemente unice
       - nu pot avea valori duplicat
       - elemente de tipuri diferite
       - este mutabila
       - nu putem modifica elemente
       - valorile setilui fiind unice sunt considerate chei
'''
data_curenta = {2023, 'noiembrie', 9, 19, 30, 'PM'}
print(data_curenta)
data_curenta.add(2022)
print(data_curenta)
data_curenta.add(2022)
print(data_curenta)

print('Adaugam un tuplu in set')
data_curenta.add((1, 2, 3))  # tuplu
print(data_curenta)

print('Eliminam un element')
data_curenta.remove(2023)
print(data_curenta)

print('Calculam lungimea setului')
lungime = len(data_curenta)
print(lungime)

'''
TUPLE - sunt de tip imutabil, nu se pot sterge/adauga/modifica valori
      - valori ordonate, indexabile
      - pot exista mai multe valori repetate
'''

tuple_numere = (1, 2, 3)
# Transformam tuplu in lista
x = list(tuple_numere)
print(type(x))

lista_litere = ['a', 'b', 'c', 'd']
print(type(lista_litere))
# Transformam  lista in tuplu
lista_litere = tuple(lista_litere)
print(type(lista_litere))
