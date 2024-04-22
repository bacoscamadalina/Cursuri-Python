# MOSTENIRE MULTIPLA

class Car:
    def go(self):
        print(f'Vrum , vrum')
    def start(self):
        print('Starting car')

class Flyable:
    def fly(self):
        print(f'Flu, flu')
    def start(self):
        print(f'Starting flyable')

class FlyingCar(Car,Flyable):
    pass

f = FlyingCar()
f.go()
f.fly()
f.start()  # o ia erarhic pe prima, nu merge mai jos - MRO (Method Resolution Order - prima metoda gasita cu numele apelat)
# daca dorim sa afisam al doilea start, schimbam denumirea