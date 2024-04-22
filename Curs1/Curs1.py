'''
acesta este un comentariu multiplu
cel simplu se face prin (#)
'''

print("Salut, lume!")  # comentariu

# Prima variabila
prima_variabila = "Prima mea variabila"
print(prima_variabila)

# Mai multe variabile cu mai multe valori
x, y, z = "Orange", "Banana", "Cherry"
print(x, y)

# Atribuim mai multor variabile o singura valoare
a = b = c = "Apple"
print(c)

# Variabila ca numar intreg, numar real, boolean, nul
numar_intreg = 10
print(numar_intreg)
numar_real = 3.14
print(numar_real)
boolean = True  # False
print(boolean)
val_nula = None
print(val_nula)

# Printam 30 de caractere
print(30 * "?")

# TIPURI DE DATE

# 1. Numar intreg - valoare de tip int (integer)
numar_intreg = 10

# 2. Numar real - valoare de tip float
numar_real = 3.14

# 3. Boolean - True / False
boolean = True  # False

# 4. Valoare de tip str (String)
x = "Alin"

# 5. Lista numere
lista_int = [1, 2, 3, 4]
lista_str = ["mere", "pere", "banane"]

# 6. Tuple
tuplu = (10, 20, 30)

# 7. Dictionar - o cheie + o valoare
dictionar = {"cheie1": "valoare1", "cheie2": "valoare2"}

# Suma dintre un numar intreg si un numar real
suma = numar_intreg + numar_real
print("Suma este: ", suma)

# Concatenam 2 siruri
nume1 = "Crina"
nume_complet = nume1 + " Munteanu"
print("Numele complet este: ", nume_complet)

'''
test_variabila = nume1 + numar_intreg
print(test_variabila)   --> va da eroare
'''

print(20 * "@")

# Functia TYPE - ne ofera tipul variabilei
print("Tipul de date al variabilei numar_intreg este:", type(numar_intreg))
print("Tipul de date al variabilei numar_real este:", type(numar_real))
print("Tipul de date al variabilei nume_complet este:", type(nume_complet))
print("Tipul de date al variabilei boolean este:", type(boolean))
print("Tipul de date al variabilei dictionar este:", type(dictionar))

# Functia type casting = conversia de tip = procesul prin care se transforma o valoare de un anumit tip intr-un alt tip de date

# Convertim un numar intreg in numar real
numar_intreg1 = 10
numar_real1 = float(numar_intreg1)
print(numar_intreg1)
print(numar_real1)
print(type(numar_real1))

# Convertim numarul in string
test_variabila1 = nume1 + " " + str(numar_intreg)
print(test_variabila1)

# Inglobarea variabilelor in cadrul instructiunii print
nume = "Ana"
an_nastere = 1992
salariu = 5000.44
print(nume, "este nascuta in anul", an_nastere, "si este angajat cu un salariu de", salariu, "lei")
print(nume + " este nascuta in anul" + str(an_nastere) + " si este angajat cu un salariu de " + str(salariu) + " lei")
print(f'{nume} este nascuta in anul {an_nastere} si este angajat cu un salariu de {salariu} lei ')

# input = este o funcție predefinită care permite interacțiunea utilizatorului, prin citirea datelor de la tastatură
#nume = input("Introdu numele tau: ")
#print(f"Salut, {nume}")

# string methods - module pe care le vom importa
sir = "ana are mere"
print(sir)

#Inlocuire
sir2 = sir.replace("mere","pere")
print(sir2)

#Sir cu litere mari
sir_mare = sir.upper()
print(sir_mare)

#Sir cu litere mici
sir_mic = sir.lower()
print(sir_mic)

# Sir despartit in lista de cuvinte
sir_split = sir.split()
print(sir_split)

#Index
sir_index = sir.index("n")
print(sir_index)

#
sir_cap = sir.capitalize()
print(sir_cap)

lista = [1,2,3,4,6]
listanr = len(lista)
print(listanr)