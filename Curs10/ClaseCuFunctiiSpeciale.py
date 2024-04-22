# CLASE CU FUNCTII SPECIALE

'''
init - este constructorul clasei
self - rept instanta curenta a clasei si este folosit pt accesa atributele clasei

'''

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):   #  conversia de la un obiect la un sir de caractere  - contine ce dorim noi in print
        return  f'Varsta : {self.age}, nume : {self.name}'  # dupa return scriem ce dorim sa afisam

    def __repr__(self):
        return str(self)
'''
METODA 1 :  __str__
         - aceasta metoda este folosita pt a defini cum va arata conversia unui obiect la un sir de caractere
         ex: cand apelam print obiect
         - stringul ne returneaza valoarea care este stocata
'''

d = Dog(1,'Nemo')
print(d)

d2 = Dog(2,'Spark')
l = [d,d2]
print(l)  # cu __repr__ i-am dat sa ne ia functia si sa o returneze

'''
METODA 2 : __repr__  (de la reprezentativ)
         - aceasta metoda este folosita pentru a oferi o reprezentare oficiala a obiectului 
'''