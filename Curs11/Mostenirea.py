# MOSTENIREA - o clasa mosteneste atributele altei clase


class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def printName(self):
        print(f'Numele meu este {self.name}.')  # pana aici avem clasa de baza


class Student(Person):  # clasa Student va mosteni tot ce avem noi in Person
    pass  # este o clasa care nu face nimic, doar mosteneste din clasa Person


p = Person('Ana', 10)  # obiect
p.printName()

s = Student('Alin', 19)
s.printName()


class Worker(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)  # mod mai modern de a apela clasa Person
        # Person.__init__(name,age) # se foloseste daca se mosteneste din mai multe clase
        self.job = job

w = Worker('Andrei',10,'inginer')
w.printName()