# Clasa care reprezinta un punct intr-un sistem de coordonate 2D

print('EX. 1')
class Punct:
    def __init__(self,x=0,y=0):  # initializam coordonatele . daca nu le modificam mai jos, x si y raman 0
        self.x = x
        self.y = y

    def muta(self,x_nou,y_nou):  # prin aceasta functie putem modifica punctele
        self.x = x_nou
        self.y = y_nou

    def __str__(self):    # ca sa ne defineasca o reprezentare a punctului printr-un sir de caractere
        return f'Punctul nou : {self.x}, {self.y}'

# Facem o istantire a clasei punct
p = Punct(1,2)
print(p)
p.muta(3,4)
print(p)


print('EX. 2')
class Masina:
    def __init__(self,marca,model,an):
        self.marca = marca
        self.model = model
        self.an = an

    def descriere(self):
        return f'Autoturismul cu marca {self.marca} , modelul {self.model} , din anul {self.an}'

    def __str__(self):
        return self.descriere()

masina_mea = Masina('Audi','A4',2009)
print(masina_mea)