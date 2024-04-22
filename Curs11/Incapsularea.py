'''
Incapsularea are trei tipuri de metode si atribute:
 - publica (accesibila peste tot)
 - privata (accesibila doar in clasa - __atribute - forma de a nota un atribut privat)
 - protected (accesibil doar in ierarhia de mostenire - _atribute )
'''


class Plane:
    __color = 'Red'

    @property  # decoratorul property transforma metoda intr-un getter pentru atributul color
    # aceasta permite accesarea valorii __ color printr-o prop denumita color
    def color(self):
        print(f'Getting value')
        return self.__color

    @color.setter  # ne permite sa luam valoarea privata si sa-i schimbam numele
    # seteaza atributul privat __color la noua valoare value
    def color(self, value):
        print(f'Setting new value')
        self.__color = value

    @color.deleter
    def color(self):
        print('Deleting value')
        self.__color = None  # reseteaza valoarea atributului privat

    @property
    def isPainted(self):
        return self.__color is not None

p = Plane()
print(p.color)

p.color = 'Blue'
print(p.color)

del p.color
print(p.color)

print(p.isPainted)
