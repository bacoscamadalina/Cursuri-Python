# Exercitii echipa - CICLURI REPETITIVE

import random
"""
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
"""
print('EX. 13 - var 1')
numar_ghicit = None
numar_secret = random.randint(0, 30)
while not numar_ghicit:
    numar_ales = int(input("Alege un numar : "))
    if numar_secret > numar_ales:
        print(f'Numarul secret este mai mare decat {numar_ales}')
    elif numar_secret < numar_ales:
        print(f'Numarul secret este mai mic decat {numar_ales}')
    else:
        print(f'Felicitari!Ai ghicit! Numarul secret este {numar_secret} și este egal cu {numar_ales} ')
        break

print('EX. 13 - var 1')
numar_secret = random.randint(1,5)
print(numar_secret)
while numar_secret == numar_secret:
    numar_ghicit =int(input('Introduceti un numar : '))
    if numar_ghicit<numar_secret:
        print('Numarul secret este mai mare')
    elif numar_ghicit>numar_secret:
        print('Numarul secret este mai mic')
    else:
        print('Ai ghicit!')
        break

'''
Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
'''
print('EX. 14')
numar = int(input('Alege un numar:'))
for i in range(1, numar + 1):
    print(str(i) * i)

'''
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
print('EX. 15')
tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for lista in tastatura_telefon:
    for j in lista:
        print(f'Cifra curenta este {j}')
