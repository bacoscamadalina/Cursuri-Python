# Polimorfism

'''
Polimorfismul se refera la abilitatea unui obiect de a se comporta in mai multe moduri in functie de context. In cazul
nostru, self stie din ce clasa este ierarhia din mosteniri.
'''


class Animal:
    def __init__(self, age, specie):
        self.age = age
        self.specie = specie

    def eat(self):
        return f' Eu sunt un {self.__class__.__name__} {self.specie} mancacios'  # returneaza numele clasei curente


class DomesticAnimal(Animal):
    def __init__(self, age, specie, owner):
        super().__init__(age, specie)
        self.owner = owner


class WildAnimal(Animal):
    def __init__(self, age, specie, location):
        super().__init__(age, specie)
        self.location = location


def animalsEat(animals):
    # ii dam o lista de animale sălbatice si iteram prin lista
    for a in animals:
        print(a.eat())


animalsEat([
    DomesticAnimal(5, 'Caine', 'Ion'),    # polimorfismul ia din ambele functii
    DomesticAnimal(6, 'Pisica', 'Ion'),
    WildAnimal(5, 'Urs', 'Pădure'),
    WildAnimal(3, 'Vulpe', 'Câmp')
])

