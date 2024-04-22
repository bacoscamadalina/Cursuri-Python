# Exercitii echipa CURS 2

# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# Definim una sau mai multe variabile, punem o conditie, daca conditia if este indeplinita, se executa blocul de cod de
# sub if, daca nu este indeplinita, se intra in else.

# 2.Verifică și afișează dacă x este număr natural sau nu.
print('EXERCITIUL 2')
x = int(input("Introducem valoarea lui x :"))
if x >= 0:
    print("Numarul este natural")
else:
    print("Numarul nu este natuarl")

# 3.Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
print('EXERCITIUL 3')
x = int(input("Introducem valoarea lui x :"))
if x > 0:
    print("Numarul este pozitiv")
elif x == 0:
    print("Numarul este neutru")
else:
    print("Numarul este negativ")

# 4.Verifică și afișează dacă x este între -2 și 13.
print('EXERCITIUL 4')
x = int(input("Introducem valoarea lui x :"))
if -2 <= x <= 13:
    print("Numarul este in interval")
else:
    print("Numarul nu se afla in interval")

# 4 - o alta varianta
if (x >= -2) and (x <= 13):
    print("Numarul este in interval")
else:
    print("Numarul nu se afla in interval")

# 5.Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
print('EXERCITIUL 5')
x = int(input("Introducem valoarea lui x :"))
y = int(input("Introducem valoarea lui y :"))
diferenta = x - y
print(diferenta)
if diferenta < 5:
    print("Diferenta este mai mica decat 5")
else:
    print("Diferenta este mai mare decat 5")

#5. alta varianta
diferenta = abs(x-y)
if diferenta < 5:
    print("Diferenta este mai mica decat 5")
else:
    print("Diferenta este mai mare decat 5")

# 6.Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
print('EXERCITIUL 6')
x = int(input("Introducem valoarea lui x :"))
if not (5 <= x <= 27):
    print("Nu se afla in intervalul mentionat")
else:
    print("Se afla in interval")

# 6. o alta variante
if x not in range(5, 27):
    print("Nu se afla in intervalul mentionat")
else:
    print("Se afla in interval")

# 7.x și y (int) .Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare
print('EXERCITIUL 7')
x = int(input("Introducem valoarea lui x :"))
y = int(input("Introducem valoarea lui y :"))
if x == y:
    print(f"{x} este egal cu {y}")
elif x > y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{x} este mai mic decat {y}")
