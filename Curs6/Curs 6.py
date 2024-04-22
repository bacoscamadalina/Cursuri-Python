# CICLURI REPETITIVE (BUCLE)

''' 
- in programare o bucla(ciclu repetitiv) este o secventa de instructiuni care se executa in mod repetat pana se 
indeplineste o anumita conditie (definita de noi)
- o bucla infinita este una fara un mod functional de oprire. Rezultatul este ca bucla se va repeta in continuu
 pana ce sistemul de operare va simti actiunea si o va termina cu o eroare
'''

# WHILE
'''
- cu bucla while putem executa un set de instructiuni pana ce conidtia este adevarata
'''
print(' Exemplul 1')
count = 0
while count < 3:
    count += 1  # daca comentez aceasta linie se va rula la nesfarsit
    print(f'count : {count}')

# iterarea prin lista - parcurgerea element cu element
print(' Exemplul 2')
l = [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(f'{l[index]}')
    index += 1

# BREAK
print(' Exemplul 3')
i = 1
while i < 6:
    print(i)
    if i == 3:
        break  # cand conditia este indeplinita se afiseaza conditia si se opreste
    i += 1

# CONTINUE
print(' Exemplul 4')
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # sare valoarea 3 - daca conditia este indeplinita, nu este luata in considerare si trece la
        # urmatoarea verificare a conditiei while
    print(i)

# WHILE - ELSE
print(' Exemplul 5')
COUNT = 0
while COUNT < 3:
    COUNT += 1
    print(COUNT)
else:
    print('sunt in else')

# ELSE - BREAK
print(' Exemplul 6')
COUNT = 0
while COUNT < 3:
    COUNT += 1
    print(COUNT)
    if COUNT == 1:
        break
else:
    print('sunt in else')

# FOR
'''
- bucla for este folosita pentru a itera o secventa (lista,tuplu,dictionar,set sau string)
'''
print(' Exemplul 7')
for i in range(10):  # va genera o secventa de la 0 - 9, fara 10
    print(i)

print(' Exemplul 8')
for i in range(5, 10):  # va genera o secventa de la 5 - 9, fara 10
    print(i)

# start - stop - step
print(' Exemplul 9')
for i in range(2, 30, 2):  # va genera o secventa de la 2 - 29, cu pasul 2, fara 30
    print(i)

# iterare prin LISTA DE ELEMENTE
print(' Exemplul 10')
l = [1, 2, 3, 4, 5]
for i in range(len(l)):
    print(l[i])

# FOR - EACH
print(' Exemplul 11')
animale = ['leu', 'caine', 'pisica']
for x in animale:  # in loc sa iteram prin index, iteram direct prin lista, iar x o sa ia valoarea fiecarui index
    print(x)

# iterare prin STRING
print(' Exemplul 12')
for x in 'Ana are mere.':  # itereaza si desparte cuvant cu cuvant
    print(x)

# iterare prin DICTIONAR
print(' Exemplul 13')
persoana = {
    'nume': 'Dan',
    'prenume': 'Andrei',
    'varsta': 30}

for x in persoana:  # iterarea se face implicit prin chei
    print(x)

print(' Exemplul 13 - b')
for x in persoana.values():  # iterare prin valori
    print(x)

print(' Exemplul 13 - c')
for x, y in persoana.items():  # iterarea se face prin cheie +valoare
    print(x, y)

# BREAK + FOR
print(' Exemplul 14')
lista = ['mere', 'pere', 'banane']
for x in lista:
    if x == 'pere':
        break
    print(x)

# CONTINUE + FOR
print(' Exemplul 15')
for x in lista:
    if x == 'mere':
        continue
    print(x)

# FOR + ELSE
print(' Exemplul 16')
for x in lista:
    print(x)
else:
    print('Sunt in else')

# ELSE + BREAK
print('EXERCITIUL 17')
for x in lista:
    if x == 'pere':
        break
    print(x)
else:
    print('Sunt in else')

# NESTED FOR
print(' Exemplul 18')
lista = ['mere', 'pere', 'banane', ' cirese']
adj = ['mari', 'galbene', 'dulci']
for x in lista:
    for y in adj:
        print(x, y)
lungime_for = len(lista) * len(adj)
print(lungime_for)

# PASS
print(' Exemplul 19')
for x in [1, 2, 3]:
    pass  # e o validare - nu face nimic

print('Exemplul 20')
for x in range(100_000_000):
    pass
print('gata')
