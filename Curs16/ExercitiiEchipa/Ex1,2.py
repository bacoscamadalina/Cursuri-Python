'''
Creeaza următoarele variabile: o lista, o tupla, un string. Itereaza prin fiecare dintre ele, prima data folosind
o bucla for, iar apoi folosind un iterator (ne vom folosi de metodele iter și next):

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(f’Primul element: {next(my_iterator)}’)
print(fAl doilea element: {next(my_iterator)}’)
print(f’Al treilea element: {next(my_iterator)}’)
print(f’Aici va da eroare: {next(my_iterator)}’)
'''
# Lista:
my_list = [1, 2, 3]
# Tupla:
my_tuple = (1, 2, 3)
# String:
my_string = 'Ana'

# Folosind bucla "FOR"
print('Folosind FOR')
# Iteram prin lista:
for i in my_list:
    print(i)

# Iteram prin tupla:
for i in my_tuple:
    print(i)

# Iteram prin string:
for i in my_string:
    print(i)

# Folosind un iterator:
print('Folosind ITERATORI')
# Iteram prin lista:
my_iterator_list = iter(my_list)
print(f'Primul element: {next(my_iterator_list)}')
print(f'Al doilea element: {next(my_iterator_list)}')
print(f'Al treilea element: {next(my_iterator_list)}')
# print(f'Aici va da eroare: {next(my_iterator_list)}')

# Iteram prin tupla:
my_iterator_tupla = iter(my_tuple)
print(f'Primul element: {next(my_iterator_tupla)}')
print(f'Al doilea element: {next(my_iterator_tupla)}')
print(f'Al treilea element: {next(my_iterator_tupla)}')
# print(f'Aici va da eroare: {next(my_iterator_tupla)}')

# Iteram prin string:
my_iterator_string = iter(my_string)
print(f'Primul element: {next(my_iterator_string)}')
print(f'Al doilea element: {next(my_iterator_string)}')
print(f'Al treilea element: {next(my_iterator_string)}')
# print(f'Aici va da eroare: {next(my_iterator_string)}')

'''
2. Atunci cand nu mai contine elemente, un iterator va arunca o excepție de tipul StopIteration. Folosește un bloc try 
except pe codul de mai sus pentru a gestiona aceasta excepție si pentru a te asigura ca programul tău ajunge la final 
cu un exit code de succes (adica 0).
'''
print('Ex. 2')
my_iterator_list = iter(my_list)
while True:
    try:
        print(f'Primul element: {next(my_iterator_list)}')
        print(f'Al doilea element: {next(my_iterator_list)}')
        print(f'Al treilea element: {next(my_iterator_list)}')
        print(f'Aici va da eroare: {next(my_iterator_list)}')
    except StopIteration:
        break

my_iterator_tupla = iter(my_tuple)
while True:
    try:
        print(f'Primul element: {next(my_iterator_tupla)}')
        print(f'Al doilea element: {next(my_iterator_tupla)}')
        print(f'Al treilea element: {next(my_iterator_tupla)}')
        print(f'Aici va da eroare: {next(my_iterator_tupla)}')
    except StopIteration:
        break

my_iterator_string = iter(my_string)
while True:
    try:
        print(f'Primul element: {next(my_iterator_string)}')
        print(f'Al doilea element: {next(my_iterator_string)}')
        print(f'Al treilea element: {next(my_iterator_string)}')
        print(f'Aici va da eroare: {next(my_iterator_string)}')
    except StopIteration:
        break