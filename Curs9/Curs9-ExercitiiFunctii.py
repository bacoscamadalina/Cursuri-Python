# EXERCITII - FUNCTII
import math

# 1.Funcție care să calculeze și să returneze suma a două numere
print('EX. 1')


def suma(a, b):
    return a + b


print(f'Suma este {suma(3, 4)}')
print(f'Suma este {suma(7, 2)}')

# o alta varianta
print('EX. 1 - alta varianta')


def calculSuma(a, b):
    suma = a + b
    return suma


print(f'Suma este {calculSuma(4, 3)}')
print(f'Suma este {calculSuma(7, 2)}')

# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
print('EX. 2')


def tipNumar(a):
    if a % 2 == 0:
        return True
    else:
        return False


print(tipNumar(2))
print(tipNumar(3))

# 3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)
print('EX. 3')


def persoana(nume, prenume, nume_mijlociu):
    return len(nume) + len(prenume) + len(nume_mijlociu)


print(persoana('Antoci', 'Ana', 'Silvia'))
print(persoana('Bacosca', 'Madalina', 'Mihaela'))

# 4. Funcție care returnează aria dreptunghiului
print('EX. 4')


def ariaDreptunghiului(l, L):
    return l * L


print(f'Aria dreptunghiului este {ariaDreptunghiului(3, 4)} m^2')
print(f'Aria dreptunghiului este {ariaDreptunghiului(7, 8)} m^2')

# 5. Funcție care returnează aria cercului
print('EX. 5')


def pi():
    return 3.14


def ariaCercului(R):
    return pi() * R ** 2


print(f'Aria cercului este {ariaCercului(3)} m^2')
print(f'Aria cercului este {ariaCercului(5)} m^2')

# 6.  Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
print('EX. 6')


def verifCaract(text, caract):
    if caract in text:
        return True
    else:
        return False


print(verifCaract('Ana are mere', 'm'))
print(verifCaract('Ana are mere', 's'))

'''
7. Funcție fără return, primește un string și printează pe ecran:
- Numărul de caractere lower case este x
- Numărul de caractere upper case exte y 
'''
print('EX. 7')


def verifString(cuvant):
    lower = 0
    upper = 0
    for i in cuvant:
        if i.islower():
            lower += 1
        else:
            upper += 1
    print(f'Numărul de caractere lower case este {lower}')
    print(f'Numărul de caractere upper case este {upper}')


verifString('StaNga')
verifString('mARea')

# 8. Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
print('EX. 8')


def lista(numar):
    lista_goala = []
    for i in numar:
        if i > 0:
            lista_goala.append(i)
    return lista_goala


print(f'Lista de numere pozitive este {lista([1, -1, 5, 2, -5])}')
print(f'Lista de numere pozitive este {lista([1, -7, -3, -2, 5])}')

'''
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
- Primul număr x este mai mare decat al doilea număr y
- Al doilea număr y este mai mare decat primul număr x
- Numerele sunt egale. 
'''
print('EX. 9')


def comparatie(x, y):
    if x > y:
        print(f'Primul număr x este mai mare decat al doilea număr y')
    elif y < x:
        print(f' Al doilea număr y este mai mare decat primul număr x')
    else:
        print(f'Numerele sunt egale. ')


comparatie(2, 3)
comparatie(6, 3)
comparatie(2, 2)

'''
10. Funcție care primește un număr și un set de numere.
- Printează ‘am adaugat numărul nou în set’ + returnează True
- Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
'''
print('EX. 10')


def adaugaNrInSet(numar, set):
    if numar in set:
        print(f'Nu am adaugat {numar} in set. Acesta exista deja')
        return False
    else:
        set.add(numar)
        print(f'Am adaugat numarul {numar} in set')
        return True


adaugaNrInSet(3, {5, 6, 2, 5})
adaugaNrInSet(4, {6, 4, 7, 3})

# 11. Funcție care primește o lună din an și returnează câte zile are acea lună.
print('EX. 11')


def pumnul(luna, an):
    if luna == 2:
        return 21
    elif luna in [4, 6, 9, 11]:
        return 30
    else:
        return 31


print(f'Luna februarie are {pumnul(2, 2022)} zile')
print(f'Luna ianuarie are {pumnul(1, 2022)} zile')

'''
12. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.

În final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
'''
print('EX. 12')


def calculator(x, y):
    suma = x + y
    diferenta = x - y
    inmultirea = x * y
    impartirea = x / y
    return suma, diferenta, inmultirea, impartirea


a, b, c, d = calculator(2, 4)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

'''
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
print('EX. 13')


def nrAparitiiCifre(lista):
    aparitii = {}
    for cifra in lista:
        if cifra not in aparitii:
            aparitii[cifra] = 1
        else:
            aparitii[cifra] += 1
    for cifra in range(0, 10):
        if cifra not in aparitii:
            aparitii[cifra] = 0
    return aparitii


lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(nrAparitiiCifre(sorted(lista)))

# 14. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele.
print('EX. 14')


def maximulNr(a, b, c):
    return max(a, b, c)


print(f'Maximul este {maximulNr(2, 4, 5)}')
print(f'Maximul este {maximulNr(8, 4, 5)}')

'''
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)
'''
print('EX. 15')


def sumaNumere(numar):
    suma = 0
    for i in range(numar + 1):
        suma += i
    print(f'Suma este {suma}')


sumaNumere(5)
sumaNumere(7)

'''
16.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''
print('EX. 16')


def numereComune(lista1, lista2):
    return set(lista1).intersection(list2)


list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
print(numereComune(list1, list2))

'''
17. Funcție care să aplice o reducere de preț.
Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
'''
print('EX. 17')


def reducere(pret, reducere):
    if 0 < reducere < 100:
        pretnou = pret - (pret * reducere / 100)
        return pretnou


print(f'Reducerea este {reducere(150, 15)} lei')
print(f'Reducerea este {reducere(250, 20)} lei')
'''
 18.Funcție care să afișeze data și ora curentă din România.
(bonus: afișazăi și data și ora curentă din China)
'''
print('EX. 18')
import time
import datetime


def dataOra():
    data_Romania = datetime.date.today()
    ora_Romania = datetime.datetime.now()
    print(f'Data Romanieie este {data_Romania}')
    print(f'Ora Romaniei este {ora_Romania.hour}:{ora_Romania.minute}:{ora_Romania.second}')


dataOra()

'''
19. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne 
zici cand e ziua ta :)
'''
print('EX. 19')
import datetime


def zilePanaLaCraciun():
    data_curenta = datetime.date.today()
    craciun = datetime.date(data_curenta.year, 12, 25)
    if craciun < data_curenta:
        craciun = craciun.replace(year=data_curenta.year)
    zile_ramase = craciun - data_curenta
    return zile_ramase.days


print(zilePanaLaCraciun())
