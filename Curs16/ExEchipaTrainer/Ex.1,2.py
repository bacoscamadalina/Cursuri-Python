'''
1. Creeaza următoarele variabile: o lista, o tupla, un string. Itereaza prin fiecare dintre ele, prima data folosind
o bucla for, iar apoi folosind un iterator (ne vom folosi de metodele iter și next):

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(f’Primul element: {next(my_iterator)}’)
print(fAl doilea element: {next(my_iterator)}’)
print(f’Al treilea element: {next(my_iterator)}’)
print(f’Aici va da eroare: {next(my_iterator)}’)


2. Atunci cand nu mai contine elemente, un iterator va arunca o excepție de tipul StopIteration. Folosește un bloc try
except pe codul de mai sus pentru a gestiona aceasta excepție si pentru a te asigura ca programul tău ajunge la final
cu un exit code de succes (adica 0).

'''


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):  # verificam daca mai sunt elemente in lista, stocam tot intr-un result
            result = self.data[self.index]  # accesam elementul curent din lista
            self.index += 1  # incrementam indexul pentru urmatoarea iteratie
            return result
        else:  # Ex 2.
            raise StopIteration


try:
    my_it = Iterator([1, 2, 3])
    while True:
        print(next(my_it))
except StopIteration:
    print('Toate elementele au fost iterate')

my_list = [1, 2, 3]
iterator = Iterator(my_list)
for item in iterator:
    print(item)

my_iterator = iter(my_list)
print(f'Primul element: {next(my_iterator)}')
print(f'Al doilea element: {next(my_iterator)}')
print(f'Al treilea element: {next(my_iterator)}')
print(f'Aici va da eroare: {next(my_iterator)}')
