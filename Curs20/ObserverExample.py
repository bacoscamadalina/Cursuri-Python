'''
                                    OBSERVER

- este un sablon comportamental care te lasa sa definesti un mecanism de tip subscriere pentru a notifica mai multe
obiecte despre un eveniment care i se intampla obiectului la care au subscris
'''

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, observable):  # va fi apleat atunci cand subiectul notifica observatorul despre o schimbare
        pass


class Observable(ABC):
    @abstractmethod
    def register_observer(self, observer):  # adaugam un observator la lista de observatori
        pass

    @abstractmethod
    def notify(self):  # notificarea observatoilor inregistrati
        pass


class Subject(Observable):
    def __init__(self, message):
        self.__message = message  # initializeaza mesajul subiectului
        # adaugam pt B
        self.observers = []

    # pentru B
    def register_observer(self, observer):
        self.observers.append(observer)  # adauga la observator

    # pentru B
    def notify(self):
        for o in self.observers:
            o.update(self)  # notificarea observatorului despre schimbare

    @property
    def message(self):
        return self.__message  # getter pentru mesaj

    @message.setter
    def message(self, msg):
        self.__message = msg  # setter pentru mesaj
        self.notify()


class RealObserverA(Observer):
    def update(self, observable):
        if observable.message.startswith('A'):
            print(f'{self.__class__.__name__} a fost notificat ')


class RealObserverB(Observer):
    def update(self, observable):
        if observable.message.startswith('B'):
            print(f'{self.__class__.__name__} a fost notificat ')


# cream instantele de observatori si a unui obiect
a = RealObserverA()
b = RealObserverB()
s = Subject('Salut')

s.register_observer(a)
s.register_observer(b)
s.message = 'Ana'
s.message = 'Barbu'
