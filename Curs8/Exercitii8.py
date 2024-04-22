# Exercitii echipa - FUNCTII

import math

# 1. Scrieţi o funcţie care primeşte ca parametru lungimea laturii unui pătrat şi returnează aria sa.
print("EX. 1")


def aria(a):
    return a ** 2


print(f'Aria patratului este : {aria(3)} ')

'''
2. Scrieţi un subprogram care primeşte ca parametru lungimea laturii unui pătrat şi returnează atât lungimea diagonalei,
cât şi perimetrul pătratului.
'''
print("EX. 2")


def diagPerim(a):
    diagonala = a * math.sqrt(2)
    print(f'Diagonala patratului este : {diagonala : .2f}')  # 2f,3f, - numarul de zecimale pe care le dorim
    perimetru = 4 * a
    print(f'Perimetrul patratului este : {perimetru}')
    return diagonala, perimetru


print(diagPerim(3))

'''
3. Scrieţi o funcţie care primeşte ca parametri de intrare lungimile celor două catete ale unui triunghi dreptunghic şi
returnează lungimea ipotenuzei.
'''
print("EX. 3")


def lungIpotenuza(a, b):
    ipotenuza = math.sqrt(a ** 2 + b ** 2)
    print(f'Ipotenuza este: {ipotenuza : .2f}')
    return ipotenuza


lungIpotenuza(2, 3)

'''
4.Scrieţi o funcţie care primeşte 3 parametri de tip real, cu semnificaţia de lungimi pentru 3 segmente. Funcţia va 
returna 1 dacă cele trei segmente pot forma un triunghi şi 0, în caz contrar.
'''
print("EX. 4")


def verifTriunghi(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return 1
    else:
        return 0


print(verifTriunghi(3, 5, 4))
