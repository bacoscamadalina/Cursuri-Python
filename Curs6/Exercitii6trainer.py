# 1. Scrie un program care foloseste o bucla for pentru a calcula suma si media unei liste de numere

print('EXERCITIUL 1')
lista_nr = [1, 2, 3, 4, 5]
suma = 0
media = 0
for numar in lista_nr:
    suma += numar  # aduna fiecare numar la suma totala
print(f'Suma numerelor este {suma}')
media = suma / len(lista_nr)
print(f'Media numerelor este {media}')

'''
2. Sa se scrie un program care citeste numerele de la tastatura pana cand se introduce numarul 0. 
Pentru fiecare numar introdus se verifica daca este par iar la final se vor afisa intr-o lista toate numerele pare.
'''
print('EXERCITIUL 2')
x = -1
lista_goala = []  # unde vom stoca numerele pare
while x != 0:  # se mai poate scrie si ( " while x " - se subantelege ca este diferit de 0)
    x = int(input('Introdu un numar : '))
    if x % 2 == 0:
        lista_goala.append(x)
print(lista_goala)

'''
3. Sa se scrie un program care citeste un text de la tastatura si va afisa un dictionar cu toate caracterele din text
in care cheile vor fi caracterele si valorile daca caracterul cheie este vocala sau consoana.
'''
print('EXERCITIUL 3')
text = input('Scrieti textul : ')
dictionar_gol = {}
for char in text:
    if not char.isalpha():  # sare peste caracterele care nu sunt litere
        continue
    char_type = ' vocala' if char.lower() in 'aeiou' else 'consoana'  # verificam daca litera este consoana sau vocala
    dictionar_gol[char] = char_type
print(dictionar_gol)

# 4. Scrieti un program care primeste o lista ca parametru si returneaza valoarea maxima din lista.

# varianta 1
lista = []
numar = int(input('Introduceti numarul oarecare: '))
for i in range(1, numar + 1):
    parametru = int(input('Introduceti parametru: '))
    lista.append(parametru)
print(f'Numarul maxim din lista este {max(lista)}')

# varianta 2
lista_parametru = [2, 12, 4, 7, 5, 100, 124, 332]
numar_maxim = lista_parametru[0]
for numar in lista_parametru:
    if numar > numar_maxim:
        numar_maxim = numar
print(f'Numarul maxim este: {numar_maxim}')
