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
    def notify(self):  # notificarea observatorilor inregistrati
        pass


class Person(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, observable):
        # vrem sa obtinem ultimul mesaj din observabil
        last_message = observable.get_last_message()
        # verificam daca mesajul incepe cu numele persoanei
        if last_message.content.startswith(self.name):
            print(f'{self.name} a primit un mesaj')

    # metoda prin care o persoana poate trimite un mesaj in chat
    def send_message(self, chatroom):
        message = input(f'{self.name} introdu un mesaj: ')
        chatroom.add_message(Message(self, message))


class Message:
    def __init__(self, autor, content):
        self.autor = autor
        self.content = content


class Chatroom(Observable):
    # facem notificare, adaugare mesaj, etc.
    def notify(self):
        for o in self.observers:
            o.update(self)

    def register_observer(self, observer):
        self.observers.append(observer)

    def __init__(self):
        self.messages = []
        self.observers = []

    def add_message(self, message):  # adaugam mesajul nou
        self.messages.append(message)
        self.notify()

    def get_last_message(self):
        return self.messages[-1]  # retuneaza ultimul mesaj din chat


c = Chatroom()
a = Person('Tom')
b = Person('Ana')
d = Person('Vasi')

c.register_observer(a)
c.register_observer(b)
c.register_observer(d)

a.send_message(c)
