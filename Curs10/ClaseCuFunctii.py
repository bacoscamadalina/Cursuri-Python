# CLASE CU FUNCTII

class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def bark(self):
        print('Hamm')

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


d = Dog(2, "Rex")
d.bark()
d.print_age()
d.print_name()
