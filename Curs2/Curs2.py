# OPERATORI

# Operatori de atribuire
x = 10
print(x)

# Operator de adunare
y = 5
# y = 5+3   - se poate asa
y += 3  # sau asa
print(y)

# Operatori de scadere
z = 10
z -= 4
print(z)

# Operator de inmultire
a = 2
a *= 5
print(a)

# Operator de impartire
b = 10
b /= 5
print(b)

# Operator de ridicare la putere
c = 3
c **= 4
print(c)

# OPERATORI ARITMETICI

# Adunare
salariu = 4325
suma_adunare = salariu + 50
print(suma_adunare)

# Scadere
suma_scadere = salariu - 50
print(suma_scadere)

# Inmultire
inmultire = salariu * 50
print(inmultire)

# Impartire
impartire = salariu / 2
print(impartire)

# Modulo
modulo = 11 % 2
print(modulo)

# Exponential
exponential = 2 ** 3
print(exponential)

# Floor division
floor_division = 10 // 3
print(floor_division)

# OPERATORI DE COMPARARE
a = 5
b = 10

# Operator de egalitate
is_equal = (a == b)
print(is_equal)

# Operator is not equal
is_notequal = (a != b)
print(is_notequal)

# Operator is less equal
c = 7
is_lessequal = (a <= c)
print(is_lessequal)

# Operator greater equal
is_greaterequal = (b >= c)
print(is_greaterequal)

# Operator less than
less_than = (a < b)
print(less_than)

# Operator greater than
greater_than = (b > c)
print(greater_than)

# OPERATORI LOGICI (and, not, or) - ordinea de prioritate este not > and > or . - not se evalueaza inaintea operat. and, or
a = 10
b = 5
c = 7
print(30 * "-")

# Utilizarea operatorului "and" intr-o expresie
rezultat_and = (a > b) and (a > c)
print(rezultat_and)

# Varianta fara paranteze
rez_and = (a > b and a > c)
print(rez_and)

# Utilizarea operatorului "or" intr-o expresie
rezultat_or = (a > b) or (a > c)
print(rezultat_or)

# Utilizarea operatorului "not" intr-o expresie
rezultat_not = not (b < a)
print(rezultat_not)

# Flow control -  IF, IF ELSE

# nota_de_trecere = 4.5
# nota = float(input('alege nota'))
# if nota >= nota_de_trecere :
# print(f'Ai luat nota {nota}')
# print('Felicitari ai trecut examenul!')
# else :
# print("Ai picat examenul")

print(30 * "-")

angajat = False
if angajat:
    print("Angajatul este prezent la serviciu")
    print("Continuam activitatile de lucru")
else:
    print("Angajatul este absent de la serviciu")
    print("Se iau masuri pentru absenta")

print(30 * "-")

# ELIF
varsta = 19
if varsta < 18:
    print("Nu esti inca major")
elif varsta == 18:
    print("Ai exact 18 ani. Felicitari pentru majorat")
elif varsta == 19:
    print("Ai 19 ani")
else:
    print("Esti major")

import datetime

an_nastere = int(input("Introduceti anul nasterii: "))
an_actual = datetime.date.today().year
varsta = an_actual - an_nastere
if varsta >= 18:
    print("Acces permis")
else:
    print("Acces restrictionat. Trebuie sa ai 18 ani")

