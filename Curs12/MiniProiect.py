'''
                                            ABSTRACTIZARE

Creați o clasa abstracta numita Gradinita care sa mosteneasca clasa ABC (abstract base class) si sa aiba urmatoarele
metode:
activitate_practica()
ora_de_somn()
Corpul primei metode va fi “pass” iar corpul celei de-a doua metode va contine un raise NotImplementedError
(estimeaza cineva ce inseamna acest raise NotImplementedError?).
Fiecare din cele doua metode vor avea decoratorul @abstractmethod (ce este un decorator?)
Implementati doua clase: GradinitaPublica si GradinitaPrivata care sa implementeze (mosteneasca) clasa abstracta
Gradinita.

Prima clasa, GradinitaPublica va rescrie ambele metode in felul urmator:
activitate_practica() va printa pe ecran: “copiii invata sa deseneze”
ora_de_somn() va printa pe ecran: “copiii trebuie sa doarma la ora cinci”

A doua clasa, GradinitaPrivata va rescrie o singura metoda in felul urmator:
activitate_practica() va printa pe ecran: “copiii invata sa modeleze cu plastilina”

Rulati codul. Se intampla ceva?
Instantiati un obiect din clasa GradinitaPublica si rulati codul. Se printeaza ceva pe ecran? De ce?
Apelati metoda activitate_practica() si rulati codul. Ce observati?
Instantiati un obiect din clasa GradinitaPrivata si rulati codul. De ce va da eroare? Cum putem sa rezolvam eroarea?
'''

# ABSTRACTIZARE
print('ABSTRACTIZARE')

from abc import ABC, abstractmethod


class Gradinita(ABC):
    @abstractmethod
    def activitatePractica(self):
        pass

    @abstractmethod
    def oraSomn(self):
        raise NotImplementedError


class GradinitaPublica(Gradinita):
    def activitatePractica(self):
        print('Copiii invata sa deseneze.')

    def oraSomn(self):
        print('Copiii trebuie sa doarma la ora 5.')


class GradinitaPrivata(Gradinita, ABC):
    '''
    Am pus ABC ca sa realizam o clasa abstracta, deoarece nu a mostenit tot din clasa Gradinita,
    tot adica activitatePractica si oraSomn. La randul ei GradinitaPrivata va deveni o clasa abstracta.
    '''

    def activitatePractica(self):
        print('Copiii invata sa modeleze cu plastilina')


# OBIECTE
p = GradinitaPublica()
p.activitatePractica()

'''
pr = GradinitaPrivata()
pr.activitatePractica()    

De ce primim eroare in acest caz?
Primim eroare deoarece clasa privata care mosteneste din Gradinita nu a implementat toate metodele abstracte din
Gradinita, asadar devine metoda abstracta.
O clasa care nu mosteneste toate metodele abstracte, va deveni o metoda abstracta
'''

'''
                                       Incapsulare
                              
Creati o noua clasa: GradinitaPublica25 care sa mosteneasca clasa GradinitaPublica. 
Implementati doar una din metode in felul urmator:
- activitate_practica() va printa pe ecran: “Copiii se joaca in curte pe balansoar”
Instantiati un obiect din clasa GradinitaPublica25.
Prin intermediul obiectului instantiat apelati metodele activitate_practica() si ora_de_somn(). 
Ce se printeaza pe ecran? De ce putem sa apelam si metoda somn? 
'''


class GradinitaPublica25(GradinitaPublica):
    numar_elevi = 100
    _adresa = 'Str.Pacii , nr.30'
    __fonduri = 20000

    @property
    def fonduri(self):
        return self.__fonduri

    @fonduri.setter
    def fonduri(self, value):  # setam o alta valoare valorii private
        self.__fonduri = value

    @fonduri.deleter
    def fonduri(self):
        self.__fonduri = None

    def activitatePractica(self):
        print('Copiii se joaca in curte pe balansoar')

    '''
                                                    POLIMORFISM

    In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de la tastatura nr de buline rosii 
    pe care le-a primit fiecare elev in parte, procesati-le si calculati media aritmetica a numarului de buline rosii.
    Daca aceasta este mai mare decat cinci, printati pe ecran: “Elevii acestei gradinite sunt foarte neastamparati”.
    Bonus:
    In interiorul clasei GradinitaPublica25 creati o noua metoda care sa primeasca de la tastatura un dictionar
    care sa contina o serie de perechi cheie:valoare si dictionare imbricate (embedded, nested) care sa contina 
    urmatoarele informatii: numele elevului, numele parintilor, varsta elevului, activitatea preferata. 
    Printati pentru fiecare elev toate informatiile de mai sus.
    '''

    def calculeazaMedieBulineRosii(self, buline):
        medie = sum(buline) / len(buline)
        if medie > 5:
            print('Elevii acestei gradinite sunt foarte neastamparati')

    def infoElevi(self):
        elevi = {}
        while True:
            nume_elevi = input('Introdu numele elevului : ')
            nume_parinti = input('Introdu numele parintilor: ')
            varsta = input('Varsta : ')
            activitate = input('Introdu activitatea preferata: ')
            elevi[nume_elevi] = {
                'Nume parinti': nume_parinti,
                'Varsta': varsta,
                'Activitate': activitate
            }
            introduce = input('Doresti sa introduci date in continuare? (y/n) ')
            if introduce.lower() != 'y':
                break
        print(elevi)


p25 = GradinitaPublica25()
p25.activitatePractica()
p25.oraSomn()
print('POLYMORPHISM')
p25.calculeazaMedieBulineRosii([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('ENCAPSULATION')
print(p25.fonduri)

p25.fonduri = 25000
print(p25.fonduri)

del p25.fonduri
print(p25.fonduri)

p25.infoElevi()
