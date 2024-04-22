'''
6. Să se tipărească toate numerele prime aflate între doi întregi citiţi. Programul va folosi o funcţie care
testează dacă un număr este prim sau nu.
'''


def is_prime(nr):
    if nr < 2:  # 1 nu este nr prim
        return False
    for i in range(2, nr):  # se mai poate scrie si range(2,nr//2+1)
        # putem face import math pt a utiliza sqrt - for i in range(2,int(math.sqrt(nr))+1)
        if nr % i == 0:  # cautam ca restul impartirii la nr cu care face iterarea sa fie egal cu 0
            return False
    return True


def print_primes_between(start, end):
    for n in range(start, end + 1):
        if is_prime(n):
            print(n)


print(print_primes_between(4, 50))

'''
7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, numere care se divid cu
suma cifrelor lor. Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.
'''
print("EX. 7")


def sumacifrelor(nr):
    suma = 0
    while nr != 0:
        ultimacifra = nr % 10  # calculeaza ultima cifra a nr folosind operatorul modulo
        print(f'Ultima cifra : {ultimacifra}')
        suma += ultimacifra
        print(f'Suma: {suma}')
        nr = nr // 10  # elimina ultima cifra a nr prin diviziunea intreaga
        print(f'Nr: {nr}')
    return suma


print(sumacifrelor(123))


def print_numbers_divisible_by_digits_sum(start, end):
    for n in range(start, end + 1):
        if n % sumacifrelor(n) == 0:
            print(n)

print(print_numbers_divisible_by_digits_sum(1,70))
