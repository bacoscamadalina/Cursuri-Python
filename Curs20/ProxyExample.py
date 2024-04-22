'''
                                             PROXY

- este un sablon structural care te lasa sa oferi un substitut pt un alt obiect
- o clasa proxy controleaza accesul la obiectul original permitand niste actiuni inainte sau dupa ce se realizeaza
actiunea obiectului original
AVANTAJE:
- poti controla obiectul original fara ca cei care il folosesc sa stie detalii despre acesta
- poti gestiona ciclul de viata al obiectului original fara a afecta clasele care il utilizeaza
- clasa Porxy functioneaza si daca obiectul original nu este pregatit sau nu este disponibil
DEZAVANTAJE:
- codul poate deveni mai complicat deoarece este nevoie de introducerea mai multor clase
- raspunsul la obiectul original poate fi intarziat in cauza clasei proxy
'''

# folosim metoda abstracta

from abc import ABC, abstractmethod


# facem o clasa abstracta care mosteneste din ABC
class Subject(ABC):
    @abstractmethod
    def request(self):  # o sa trebuiasca sa fie suprascrisa de subclase
        pass


class RealSubject(Subject):
    def request(self):
        print('Real subject: ma ocup de request')


# facem clasa proxy care ofera un inlocuitor pentru real subject
class Proxy(Subject):
    def __init__(self, rs):
        self.real_subject = rs

    def check_acces(self):
        print('Proxy: verificam acces pt request')
        return True  # accesul este intotdeauna permis

    def log_request(self):  # metoda aditionala pt logare
        print('Proxy: se afișează timpul requestului')

    # facem functia care ne intereseaza cel mai mult
    def request(self):
        if self.check_acces():  # verificam accesul
            self.real_subject.request()
            self.log_request()


# cream o instanta
rs = RealSubject()
rs.request()


print(30*'--')
Proxy = Proxy(rs)
Proxy.request()