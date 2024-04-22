'''
                                           - ITERATORI -
1. Implementati un iterator numit ReverseIterator, care parcurge o colecție in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d
'''
print('EX 1.')


class ReverseIterator:
    def __init__(self, collection):  # collection = colectia pe care se doreste sa se faca iterarea
        self.collection = collection
        self.start = len(collection) - 1  # seteeaza indexul la ultimul element al colectiei

    def __iter__(self):
        return self  # returneaza instanta iteratorului

    def __next__(self):
        if self.start < 0:  # verificam daca indexul start este mai mic decat 0
            raise StopIteration
        currentindex = self.start  # stocam variabila initiala in currentindex
        self.start -= 1  # decrementam indexul start
        return self.collection[currentindex]  # returneaza elementul curent din colectie


note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
print(next(rev_it))  # printeaza 7

print('Cu for')
for i in rev_it:
    print(i)

'''
                                         - GENERATOR - 
2. Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da câte un număr intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
'''
print('EX 2.')
from random import randint

print('Cu dubluri')


def loterie_gen():
    for i in range(6):
        yield randint(1, 49)
    yield randint(1_000_000, 9_999_999)


for i in loterie_gen():
    print(i)

print('Stocate in SET')


def loterie_gen():
    generate = set()
    for i in range(6):
        nr = randint(1, 49)
        while nr in generate:  # cat timp numarul generat a mai fost generat o data
            nr = randint(1, 49)
        generate.add(nr)
        yield nr
    yield randint(1_000_000, 9_999_999)


for i in loterie_gen():
    print(i)

'''
                                         - DECORATORS - 
4. Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printează argumentele de intrare, și rezultatul unei funcții
'''
print('EX 4.')
import functools
from time import perf_counter, sleep


# Functia timeit
def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()  # ne ia ora calculatorului
        result = func(*args, **kwargs)
        print(f'A durat {perf_counter() - start} secunde')
        return result

    return wrapper()


@time_it
def sayHello():
    sleep(3)
    print('Functie executata')


# Functia logger

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # ne arata care din imputurile noastre sunt args si care sunt kwags
        print(f'Rezultat : {result}')
        print(f'Argumente pozitionale : {args}')
        print(f'Argumente cu nume : {kwargs}')

    return wrapper


@logger
def name(first, last):
    return f'{first} - {last}'


name('Ana', last='Anton')
name('Ana', {'last': 'Anton'})
name('Ana', 'Anton')

'''
                                          - DECORATORS EXTRA -
5. Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi nume, email, parola, și data nasterii 
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat, folosind un decorator
`@require_login` 
– o metoda logout, fara params, care delogheaza userul.
Se va tasta apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
'''
print('EX 5.')


def require_login(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_logged_in:
            return func(self, *args, **kwargs)
        else:
            return 'Utilizatorul nu este logat'

    return wrapper


class User:
    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.__logat = False  # consideram ca userul intrat in aplicatie nu este logat

    def login(self, email, parola):  # daca sunt corecte, userul va fi considerat logat
        if email == self.email and parola == self.parola:
            self.__logat = True

    @require_login
    def getinfo(self):
        return f'Nume : {self.nume}, email : {self.email}, data nasterii : {self.data_nasterii}, parola :{"*" * len(self.parola)}'

    def logout(self):
        self.__logat = False

    @property  # dam dreptul decoratorului sa acceseze functia privata
    def is_logged_in(self):
        return self.__logat  # ne returneaza parametrul


u = User('Ana Maria', 'anamaria@yahoo.com', 'anamaria1991', '19-02-1991')
print(u.getinfo())
u.login('anamaria@yahoo.com', 'anamaria1991')
print(u.getinfo())
u.logout()
print(u.getinfo())

'''
6. Sa se scrie un decorator care primeste ca parametru doua ore,
reprezentand datele limita intre care sa se execute functiile decorate.
'''
print('Ex. 6')
import datetime


def only_execute_between(start, end):
    def decorator_execute_between(func):
        def wrapper(*args, **kwargs):
            if start <= datetime.datetime.now().hour <= end:
                return func(*args, **kwargs)

        return wrapper

    return decorator_execute_between  # returneaza functia interna a decoratorului


@only_execute_between(16, 17)
def hello():
    print('Hello Word!')


hello()
