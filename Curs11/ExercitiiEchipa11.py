# EXERCITII ECHIPA - PILONII OOP

'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional,
doar dacă ai ales să implementezi metoda abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui
'''

# ABSTRACTION

from abc import ABC, abstractmethod
from math import pi


class FormaGeometrica(ABC):
    PI = pi

    @abstractmethod
    def aria(self):
        pass

    def descriere(self):
        print(f'Cel mai probabil am colturi')


# INHERITANCE + ENCAPSULTION

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura  # am facut latura ca fiind privat
        print(f'Initul clasei patrat')

    def aria(self):
        return self.__latura ** 2

# ENCAPSULATION

    # GETTER
    @property
    def latura(self):
        return self.__latura

    # SETTER
    @latura.setter
    def latura(self, new_latura):
        self.__latura = new_latura

    # DELETER
    @latura.deleter
    def latura(self):
        self.__latura = None
        print('Am sters latura')


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        return self.PI * (self.__raza) ** 2

    # GETTER
    @property
    def raza(self):
        return self.__raza

    # SETTER
    @raza.setter
    def raza(self, new_raza):
        self.__raza = new_raza

    # DELETER
    @raza.deleter
    def raza(self):
        self.__raza = None
        print('Am sters raza')

    def descriere(self):
        print('Eu nu am colturi')


# POLYMORPHISM
def descriereInterfata(obj):  # functie ce apeleaza obiectul si ne preia descrierea
    obj.descriere()


# OBIECTUL PATRAT
print('OBIECTUL PATRAT')

p = Patrat(5)
p.descriere()
print(f'Aria este {p.aria()}')
print(f'Latura este {p.latura}')
p.latura = 7
print(f'Aria este {p.aria()}')
print(f'Latura este {p.latura}')
del p.latura

# OBIECTUL CERC
print('OBIECTUL CERC')
c = Cerc(7)
p.descriere()
print(f'Raza este {c.raza}')
print(f'Aria este {c.aria()}')
c.raza = 8
print(f'Raza este {c.raza}')
print(f'Aria este {c.aria()}')
del c.raza

print('POLYMORPHISM')
descriereInterfata(p)
descriereInterfata(c)
