'''
1. printare
str = "Salut"
print str

Eroare: Missing parentheses in call to 'print'. Did you mean print(...)?
'''
print('Ex 1.')
str = "Salut"
print(str)

'''
2. for
for elem in [1,2,3,4,5]
print(elem)
SyntaxError: expected ':'

'''
print('Ex 2.')
for elem in [1, 2, 3, 4, 5]:
    print(elem)

'''
3.  clasa
class Student:
def init(self, name):
self.name = name
#
s = Student
print(s.name)


# AttributeError: type object 'Student' has no attribute 'name'
'''
print('Ex 3.')


class Student:
    def __init__(self, name):
        self.name = name


#
s = Student('Ana')
print(s.name)

'''
4. open
with open("file.txt") as f:
    f.write("salut")
    
FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'   
'''
print('Ex 4.')
with open("file.txt", 'w') as f:
    f.write("salut")

'''
5. indexing
i = [1, 2, 3, 4, 5, 6]
print(i[6])

IndexError: list index out of range
'''
print('Ex 5.')
i = [1, 2, 3, 4, 5, 6]
print(i[5])


'''
6. slicing
string = "Salut"
print(string[5:6])

'''
print('Ex. 6')
string = "Salut"
print(string[2:4])

# s  a  l  u  t
# 0  1  2  3  4
#-5 -4 -3 -2 -2

print(string[-5])
print(string[2:5:2])
print(string[::-1])

'''
7. inheritance
class Animal:
     def roar(self):
         pass

class Lion(Animal):
    def roar(self):
        pass

'''
print('Ex. 7')

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def roar(self):
        pass   # clasa abstracta

class Lion(Animal):
    def roar(self):
        print('Roar')


leu = Lion()
leu.roar()

'''
8. collections
l = [1, 2, 3]
t = ("a", "b", "c")
s = {2, 3, 4}
print(type(l), type(t), type(s))
'''
print('Ex 8')
l = [1, 2, 3]
t = ("a", "b", "c")
s = {2, 3, 4}
print(type(l), type(t), type(s))

# la set nu putem folosi index


'''
9. Generator
def gen(n):
    for i in range(n):
        if i % 2 == 0:
            return i

for even in gen:
    print(even)
    
    
TypeError: 'function' object is not iterable
'''
print('Ex. 9')

def gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for even in gen(7):
    print(even)




'''
1. Ce inseamnă acronimul 00P in programare?

a. Original Object Programming
b. Object-Oriented Programming
c. Object-Oriented Python
d. Oriented Object Processing


1.b


2. Ce este un obiect in Python?
a. O funcţie
b. O instanţă a unei clase
c. Un tip de date primitiv
d. Un modul extern

2.b


3. Ce reprezintă "self" in metodele unei clase in Python?

a. Referința la instanţa curentă a clasei
b. Un cuvânt rezervat pentru definirea claselor
c. Un argument opțional în orice metodă
d. Un sinonim pentru "super"


3.a (folosit pt a accesa o variabila)


4. Ce este moştenirea in contextul programării orientate pe obiect in Python?

a. Capacitatea de a accesa metode private ale unei clase părinte
b. Transmiterea caracteristicilor şi comportamentului de la o clasă părinte la o clasă copil c. O metodă specială
 pentru crearea obiectelor
d. Un decorator pentru metodele clasei



4.b


5. Ce este un constructor in Python?

a. O funcție care distruge un obiect
b. o metodă care întoarce valoarea unui atribut al unui obiect
c. O metodă specială pentru iniţializarea obiectelor
d. Un decorator pentru metode


5.c



6. Ce face instrucțiunea super() in Python?

a. Referință la clasa curentă
b. Accesează metodele clasei părinte
c. Creează o instanţă a clasei curente
d. Schimbă comportamentul operatorului "or"

6.b


7. Cum se creează o instanță a unei clase in Python?

a. Apeland numele clasei ca şi cum ar fi o funcție
b. Folosind funcţia 'create_instance()
c. Utilizând cuvântul cheie "instance_of"
d. Prin intermediul metodei new_instance() a clasei


7.a


8. Care este scopul metodei str__ in Python?

a. Transformă un obiect în şir de caractere
b. Returnează un şir formatat de caractere pentru afişare
c. Verifică dacă două obiecte sunt identice
d. Este un sinonim pentru metoda __init__


8.b

9. Ce reprezintă conceptul de incapsulare in OOP?

a. Ascunderea detaliilor interne ale unei clase şi expunerea unei interfeţe clare
b. Crearea unor obiecte complexe prin combinarea a mai multor obiecte simple
c. Transmiterea caracteristicilor de la o clasă părinte la o clasă copil
d. O tehnică de programare funcţională

9.a

10. Ce este polimorfismul in Python?

a. Posibilitatea unei clase de a avea mai mult de un constructor
b. O tehnică de gestionare a excepțiilor
c. Utilizarea mai multor fire de execuţie pentru a accelera programul
d. Capacitatea unui obiect de a lua mai multe forme, adică de a fi tratat ca un obiect de mai multe tipuri


10.d

'''


