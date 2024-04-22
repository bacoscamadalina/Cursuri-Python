#                            ITERATORI

'''
next() -> merge prin iterare, ia fiecare element din lista si il afiseaza
iteratori : for, while,for each, if
Metoda speciala: __iter__  - necesara pt a crea un iterator
'''


# Generarea numerelor pare

class Eveniterator:
    def __init__(self, n):
        self.n = n  # n = nr total de nr pare pe care dorim sa le generam
        self.generatednumbers = 0  # contor
        self.curentnumber = 0  # numarul curent care este verificat daca este par

    def __iter__(self):
        return self  # returneaza instanta iteratorului

    def __next__(self):  # metoda apelata pt a obtine urmatorul element din iterator
        self.curentnumber += 1  # incrementam
        # verificam daca nr de numere generate a ajuns la nr par, adica daca s-a ajuns la limita n
        if self.generatednumbers >= self.n:
            raise StopIteration  # ii dam o exceptie cand s-a atins limita
        # verificam daca nr curent este par
        if self.curentnumber % 2 == 0:
            self.generatednumbers += 1
            return self.curentnumber
        return self.__next__()  # daca nr este par, apelam recursiv functia next


it = Eveniterator(15)
for i in it:
    print(i)

