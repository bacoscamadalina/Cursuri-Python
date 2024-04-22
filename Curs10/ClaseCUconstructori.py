# CLASE CU CONSTRUCTORI

class Cat:
    specie = 'Mamifer'

    # Constructorul se formeaza printr-o functie:
    def __init__(self,age,name):  # standard pt contructor (init = initializare)
        # aici vom crea atributele de instanta
        self.age = age  # self este o referinta catre obiectul curent
                        # self.age = age este o conventie si putem avea self.age = varsta. Dar lasam asa sa fie citet
        self.name = name
c1 = Cat(1,'Garfield')
c2 = Cat(2,'Tom')

print(f'Cat 1 age: {c1.age} ,Cat 2 age: {c2.age}')
print(f'Cat 1 name: {c1.name} ,Cat 2 name: {c2.name}')
print(f'Specie: {Cat.specie}')
# print(f'Nume: {Cat.name}')   # va da eroare deoarece se afla in atributul de construtor, nu de clasa
