import datetime

'''
1.Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)

'''
print('Ex 1.')


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        return f' Nume : {self.nume} , prenume : {self.prenume}, salariu: {self.salariu}'

    def nume_complet(self):
        return f' Nume : {self.nume} , prenume : {self.prenume}'

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return 12 * self.salariu

    def marire_salariu(self, procent):
        self.salariu += self.salariu * procent / 100
        return self.salariu

    def __str__(self):
        return f'{self.nume}, {self.prenume}, salariul: {self.salariu}'


angajat = Angajat('Ana', 'Anton', 3000)
angajat.marire_salariu(50)
print(angajat)

'''
2. Clasa Factură
      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), 
     număr, nume_produs, cantitate, pret_buc
      Constructor: toate atributele, fără serie
     Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000 
'''
print('Ex 2. - varianta 1')


class Factura:
    serie = '24341'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitate(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        total = self.cantitate * self.pret_buc
        data_curenta = datetime.datetime.now()
        print(f'Factura seria : {self.serie} , numar : {self.numar} ')
        print(f'Data : {data_curenta}')
        print('Produs | Cantitate | Pret bucata | Total')
        print(f'{self.nume_produs} | {self.cantitate} | {self.pret_buc} | {total}')

        print(5 * '-')

        print("Factura seria", self.serie, "numarul", self.numar)
        print("Data:", data_curenta)
        print("Produs\t|\tCantitate\t|\tPret bucata\t|\tTotal")
        print(self.nume_produs, "\t|\t", self.cantitate, "\t\t|\t", self.pret_buc, "\t\t|\t", total)


factura = Factura(7, 'Telefon', 9, 2500)
factura.genereaza_factura()
factura.schimba_cantitate(20)
factura.schimba_pretul(3000)
factura.genereaza_factura()

from tabulate import tabulate
print('Ex 2. - varianta 2')


class Factura:
    serie = '24341'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitate(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        data_curenta = datetime.datetime.now()
        total = self.cantitate * self.pret_buc
        header = ['Produs', 'Cantitate', 'Pret bucata' , 'Total']
        data = [[self.nume_produs,self.cantitate,self.pret_buc,total]]
        print(f'Seria factura :', Factura.serie , 'numarul : ', self.numar)
        print('Data curenta: ', data_curenta)
        print(tabulate(data,headers = header, tablefmt='grid'))

f1 = Factura(7, 'Telefon', 9, 2500)
f1.genereaza_factura()
