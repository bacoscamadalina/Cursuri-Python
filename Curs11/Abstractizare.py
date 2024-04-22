# ABSTRACTIZARE


'''
O clasa abstracta are cel putin o metoda abstracta
O metoda abstracta este o metoda fara impelementare (fara corp)
Avem nevoie sa importam pachetul "ABC"
'''

'''
Abstractizarea = definirea unui set de caracteristici (metode) care trebuie sa fie implementata de orice clasa concreta
                 ce mosteneste clasa abstracta, asigurand o uniformitate si coerenta in comportamentul tuturor
                 subclaselor
'''

from abc import ABC, abstractmethod  # primul pas pt aa utiliza metodele abstracte


class Animal(ABC):
    # pentru a utiliza o metoda abstracta utilizam un decorator (marcat cu galben)
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError  # exceptie


# ex: ni se cere o formă geometrica - o clasa abstracta contine toate figurile geometrice

class Dog(Animal):
    def sound(self):
        print(f'Uff')

    def sleep(self):
        print(f'ZZZZ')


d = Dog()
d.sound()
d.sleep()
