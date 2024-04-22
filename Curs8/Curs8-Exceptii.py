# EXCEPTII

# print(1/0)  --> ZeroDivisionError: division by zero
# print(x)    --> NameError: name 'x' is not defined

"""
try: (Blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului Try)
except NumeEroare: <-- printarea tuturor exceptiilor de tipul NumeEroare
    se executa daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): <-- Gruparea mai multor tipuri de exceptii
    se executa daca se prinde AltNumeEroare say IncaUnNumeEroare
except Eroarea4 as ex: <-- Stocarea mesajului unei erori intr-o variabila (exemplul variabilei "ex")
    se poate accesa mesajul de Eroare
else:
    se executa doar daca nu se arunca eroare in blicul try
finally:
    se executa indiferent daca se arunca eroare sau nu.
"""

# TRATAREA ERORILOR - incepe prin blocul "try"

# TRY - EXCEPT
try:
    print(x)
except:
    print('A aparut o eroare')

print(30 * '-')

# TRY - MULTIPLE EXCEPT
try:
    print(str.values)
except NameError:
    print('Variabila x nu este definita')
except ZeroDivisionError as ex:
    print(f'Eroare: {ex}')
except:
    print('A aparut o alta eroare')

print(30 * '-')

# TRY - EXCEPT - ELSE
try:
    print(3)
except:
    print('A aparut o eroare')
else:
    print('Nu a aprut nici o eroare')

print(30 * "-")

# TRY - EXCEPT - FINALLY
try:
    print(x)
except:
    print('A aparut o eroare')
finally:
    print('Eu sunt executat mereu')

print(30 * "-")

# PROVOCAREA ERORILOR
x = -1
if x < 0:
    raise Exception('Fara numere negative')
