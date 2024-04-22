# EXERCITII ECHIPA

# 1.Funcție care să calculeze și să returneze suma a două numere
print("EX. 1")


def suma(a, b):
    return (a + b)


print(f'Suma dintre a si b este {suma(3, 4)}')
print(f'Suma dintre a si b este {suma(6, 7)}')

# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar
print("EX. 2")


def parimpar(a):
    if a % 2 == 0:
        return True
    else:
        return False


print(parimpar(2))
print(parimpar(3))

# 3. Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)
print("EX. 3")


def numecomplet(nume, prenume, nume_mijlociu):
    return len(nume) + len(prenume) + len(nume_mijlociu)


print(numecomplet('Bacosca', 'Madalina', 'Mihaela'))
print(numecomplet('Susanu', 'Ana', 'Alina'))

'''
5.Scrieţi o funcţie care returnează prima cifră a unui număr natural. De exemplu, dacă parametrul efectiv este 127,
funcţia va returna 1.
'''
print("EX. 5")


def primaCifra(nr):
    return int(str(nr)[0])

print(f'Prima cifra a numarului este {primaCifra(123)}')
print(f'Prima cifra a numarului este {primaCifra(354)}')

'''
6. Să se tipărească toate numerele prime aflate între doi întregi citiţi. Programul va folosi o funcţie care 
testează dacă un număr este prim sau nu.
'''
print("EX. 6")


def numereprime(nr1, nr2):
    listanr = []
    for numar in range(nr1 + 1, nr2):
        for i in range(2, numar):
            if numar % i == 0:
                break
        else:
            listanr.append(numar)
    return listanr


print('Numere prime:', numereprime(4, 50))

'''
7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, numere care se divid cu 
suma cifrelor lor. Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.
'''
print("EX. 7")
def suma_cifrelor(numar):
    suma = 0
    while numar > 0:
        suma += numar % 10
        numar //= 10
    return suma



print(suma_cifrelor(1234))