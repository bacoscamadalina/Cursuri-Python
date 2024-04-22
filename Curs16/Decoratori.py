#                                              DECORATORI
# VERIFICAM TIMPUL DE RULARE A UNEI FUNCTII
import functools
import time


def timpDeExecutie(functieoriginala):
    @functools.wraps(functieoriginala)
    # in mom in care noi decoram o alta functie cu fct noastra, in consola o sa arate numele functiei cu decoarator,
    # wraps ne pastreaza numele original, el stie sa grupeze si stiu ce fac fiecare
    def wrapper(*args, **kwargs):  # ne iau toate posibilitatile de parametre
        t1 = time.time()  # ne ia timpul serverului (data si ora la milisecunde) si stocheaza in t1
        result = functieoriginala(*args, **kwargs)  # ne ia timpul, ruleaza functia si dupa ia inca un timp,t2
        t2 = time.time() - t1  # durata de timp in care functia originala va rula
        print(f'{functieoriginala.__name__} a fost executata in {t2} secunde')
        return result

    return wrapper  # returneaza functia wrapper


@timpDeExecutie
def afisareInformatii(nume, varsta):
    time.sleep(1)  # daca noi vom rula functia, va rula repede a.i vom primi 0.00. Facem un delay fortat
    print(f'Afisare informatii. A rulat cu parametrii {nume} si {varsta}.')


a = afisareInformatii('Ana', 16)
print(a)


# Sa se scrie un decorator care repeta functia de doua ori

def doTwice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # fortam sa mai ruleze o data
        return func(*args, **kwargs)

    return wrapper


@doTwice
def returnGreeting(nume):
    print('Create greeting')
    return f'Hi {nume}'


r = returnGreeting('Ana')
print(r)


def logare(functie):
    def wrapper(*args, **kwargs):
        print(f"A fost apelată funcția {functie.__name__} cu argumentele {args} și keyword-urile {kwargs}")
        rezultat = functie(*args, **kwargs)
        print(f"Funcția a returnat: {rezultat}")
        return rezultat

    return wrapper


@logare
def adunare(a, b):
    return a + b


adunare(2, 3)





def memorare_cache(functie):
    cache = {}

    def wrapper(*args, **kwargs):
        cheie = (args, frozenset(kwargs.items()))
        if cheie not in cache:
            cache[cheie] = functie(*args, **kwargs)
        return cache[cheie]

    return wrapper

@memorare_cache
def operatie_lenta(x, y):
    print("Executând operație lentă...")
    return x * y

operatie_lenta(2, 3)  # Va afișa "Executând operație lentă..."
operatie_lenta(2, 3)  # Nu va mai executa operația lentă, ci va returna rezultatul din cache
