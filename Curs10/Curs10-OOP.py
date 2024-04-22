# CURS 10 - OOP

'''
CLASA - este o schita sau un prototip definita de un programator in care sunt create obiecte
      - ofera un mijloc de a grupa  datele si functionalitatile
      - crerea unei clase noi creaza un nou tip de obiect, permitand instantierea unor oboiecte din acest tip
      (instantiere = crearea unui obiect)

Fiecare instanta de clasa poate avea atribute atasate pt mentinerea starii sale. Instantele de clase pot avea si metode
pt modificarea starii lor.

OBIECT - este instanta unei clase

Diferenta intre obiect si clasa:
- o clasa este ca o schita
- un obiect este o copie a clasei cu valori reale
'''

class Dog:  # clasa Dog, se scrie cu litera mare
    # atributele clasei:
    specie = 'mamifer'
    varsta = 6
    nume = 'Bruno'

# instantierea unui obiect
d = Dog()
print(type(d))
print(d.specie)  # d.specie class.atribut
print(d.varsta)
print(d.nume)

d2 = Dog()
d2.nume = 'Pufi'  # name pt d2 devine atribut de instanta pt obiectul d2 (nu se mai poate modifica numai prin d2)
print(f'Nume d: {d.nume},Nume d2 : {d2.nume}')

Dog.nume = 'Rex' # schimbarea atributului de clasa nu are efect asupra atributului de instanta
print(f'Nume d: {d.nume},Nume d2 : {d2.nume}')


