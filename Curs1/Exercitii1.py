# Exercitii echipa CURS 1

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabila este ca un "depozit" in care depozitam tot felul de alimente.

#2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:string,int,float,bool
print('EXERCITIUL 2')
string = "Antonia"
print(string)
integer = 2
print(integer)
real = 1367.43
print(real)
bool = True
print(bool)

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print('EXERCITIUL 3')
print(type(string))
print(type(integer))
print(type(real))
print(type(bool))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia.
print('EXERCITIUL 4')
real_rotunjit = round(real)
print(real_rotunjit)
print(type(real_rotunjit))

# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
print('EXERCITIUL 5')
print('Este %s că dacă %s are %s copii, ei vor primi o alocație în valoare de %s lei' % (bool, string, integer, real))
print(f'Este {bool} că dacă {string} are {integer} copii, ei vor primi o alocatie in valoare de {real} lei')
print("Este " + str(bool) + " ca daca " + string + " are " + str(
    integer) + " copii, ei vor primi o alocatie in valoare de " + str(real) + " lei ")
print("Este ", bool, " ca daca ", string, " are ", integer, " copii, ei vor primi o alocatie in valoare de ", real,
      " lei ")

# 6. Citește de la tastatură: numele,prenumele.  Afișează: 'Numele complet are x caractere'.
print('EXERCITIUL 6')
numele = input("Nume:")
prenumele = input("Prenume:")
nume_complet = numele + prenumele
print(f'Numele complet este {numele} {prenumele}.')
print(f'Numele complet are {len(nume_complet)} caractere.')
