# FUNCTII

"""
DEF: O functie in Python este un bloc de cod care este proiectat pentru a executa o anumita sarcina.
   Functia se defineste o singura data, iar apoi poate fi apelata de mai multe ori, in orice program, permitand
reutilizarea codului.
   Functiile ajuta la organizarea si structurarea codului si pot primi date de intrare (numite ARGUMENTE) si pot returna
date de iesire (prin intermediul valorii returnate).
   Notatia pentru a defini functia este "def"
"""


# FUNCTIE SIMPLA
def my_Function():  # signatura functiei (contine numele ei si orice poate aparea in paranteze)
    # in interiorul functiei vom scrie corpul functiei
    print(f'Hello din functie')


my_Function()  # apelare prin adaugarea de paranteze, daca nu se pun, nu se apeleaza


# FUNCTII CU PARAMETRI
def say_Hi(name):
    print(f'Hi, {name}')


say_Hi('Ana')


# FUNCTIE CU DOI PARAMETRI
def arata_Suma(a, b):
    print(f'Suma este {a + b}')


arata_Suma(2, 3)


# AFISAREA CHEILOR DINTR-UN DICTIONAR
def show_Keys(dct):
    print(dct.keys())
    print(dct.values())


show_Keys({'A': 1, 'B': 3})

# FUNCTIE CU RETURN
'''
   Return intr-o functie Python este folosit pentru a specifica ce valoare va fi trimisa inapoi la codul care a apelat
functia.
   Este ca si cum ai spune "Dupa ce am terminat tot ce trebuie sa  fac in functie, voi da inapoi aceasta valoare."
   Acest lucru ajuta la transferul de informatii intre diferite parti ale unui program si face ca functiile sa fie mai
utile, deoarece pot da un rezultat pe care il poti folosi in alte locuri in codul tau.
   Return stocheaza informatia pentru a putea fi refolosita. 
'''


def say_Hello():
    return 'Hello!'


# functia se opreste din executie si se va intoarce in locul in care a fost apelata dand inapoi valoarea 'Hello'

# Prima varianta de afisare
text = say_Hello()
print(text)
# A doua varianta de afisare
print(say_Hello())


def say_Hi2():
    print('Hi')


textt = say_Hi2()
print(textt)
# None apare deoarece nu am dat return - functia nu retine nimic

print(30 * '-')


# FUNCTII CU PARAMETRI SI RETURN
def produs(a, b):
    return a * b


p = produs(3, 2)
print(p)


def isEven(number):
    # if number % 2 == 0:     <-- varianta mai complicata
    #       return True
    #   return False
    return number % 2 == 0  # varianta mai simpla


# Apelam o functie in alta functie
def getAllEvenNumbers(numbers):
    result = []
    for elem in numbers:
        #        if elem % 2 == 0:
        if isEven(elem):
            result.append(elem)
    return result


nr = getAllEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(nr)


# TIPURI DE PARAMETRI


def plus(a, b):  # a, b sunt parametri (numele folosite pentru argumentele unei functii)
    return a + b


plus(1, 2)  # 1,2 sunt argumente (argumentele sunt valorile parametrilor)


# DEFAULT ARGUMENTS (parametri cu valori implicite)
def plus(a, b=2):  # lui "b" i-am dat noi valoare
    return a + b


print(plus(2))  # daca nu specificam o valoare explicita pt b, atunci va lua valoarea implicita 2
plus(3, 4)  # daca ii dam o alta valoare atunci va ignora valoarea din functie


# KEY WORD ARGUMENTS
def plus(a, b):
    return a + b


plus(a=1, b=2)
plus(b=2, a=1)


# specificand argumentele prin numele lor, nu mai este necesar sa pastram ordinea atata timp cat ii pastram pe toti


# NUMAR VARIABIL PE PARAMETRI
def plus(*args):  # args e o conventie, conteaza steluta
    print(args)
    return sum(args)


plus(1, 2, 3)
plus(*[1, 2, 3])  # * - se numeste unpacking, adica scoate elementele dintr-o colectie


# KEY WORD ARGUMENTS
def plus(**kwargs):  # kwargs este un dictionar care contine toate argumentele date functiei
    print(kwargs)
    suma = sum(kwargs.values())
    print(f'Suma este: {suma}')
    return suma


plus(a=1, b=2)


def exemplu(*args, **kwargs):
    print(f'args: {args},kwargs: {kwargs}')
    suma_args = sum(args)
    print(f'suma_args: {suma_args}')
    suma_kwargs = len(kwargs)
    print(f'suma_args: {suma_kwargs}')


exemplu(1, 2, 3, a=4, b=5, c=6, *[4,5,6])
