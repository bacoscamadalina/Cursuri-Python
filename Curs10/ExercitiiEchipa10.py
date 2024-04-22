# EXERCITII ECHIPA

'''
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()
'''
print('EX. 1')

import math


class Cerc:
    def __init__(self, raza, culoare):  # initializam constructorul clasei Cerc
        self.raza = raza  # accesam atributele clasei
        self.culoare = culoare

    def descrierecerc(self):
        return f'Culoarea este {self.culoare}, iar raza este de {self.raza} m '

    def aria(self):
        return f'Aria este {math.pi * self.raza ** 2} m^2'

    def diametru(self):
        return f'Diametrul este {2 * self.raza} m'

    def circumferinta(self):
        return f'Circumferinta cercului este {2 * self.raza * math.pi} m'

    def __str__(self):
        return self.descrierecerc()


cercul_meu = Cerc(3, 'Galben')
print(cercul_meu)
print(cercul_meu.aria())
print(cercul_meu.diametru())
print(cercul_meu.circumferinta())

'''
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va
suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
'''
print('EX. 2')


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return f'Dreptunghiul are urmatoarele dimensiuni : lungime {self.lungime} m , latime {self.latime} m, culoare {self.culoare}'

    def aria(self):
        return f'Aria este {self.lungime * self.latime} m^2'

    def perimetru(self):
        return f'Perimetrul este {2 * self.latime + 2 * self.latime} m'

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua

    def __str__(self):
        return self.descriere()


dreptunghiul_meu = Dreptunghi(3, 2, 'Rosu')
print(dreptunghiul_meu)
print(dreptunghiul_meu.aria())
print(dreptunghiul_meu.perimetru())

dreptunghiul_meu.schimba_culoarea('Verde')
print(dreptunghiul_meu)

# Construiti o clasa Student care sa afiseze numele studentului si media.
print('EX. 3')


class Student:
    def __init__(self, nume):
        self.nume = nume
        self.note = []

    def adaugaNota(self, nota):
        self.note.append(nota)

    def medie(self):
        if self.note:
            return sum(self.note) / len(self.note)
        else:
            return 0

    def __str__(self):
        return f'Student : {self.nume}, medie : {self.medie():.2f}'


s = Student('Ion')
s.adaugaNota(int(input('Nota: ')))
s.adaugaNota(int(input('Nota: ')))
print(s)
