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

    def descrie(self):
        return print(f'Numele meu este {self.nume} {self.prenume}, iar salariul meu este de {self.salariu} lei')

    def numeComplet(self):
        return print(f'Numele meu complet este {self.nume} {self.prenume}')

    def salariuLunar(self):
        return print(f'Salariul meu lunar este {self.salariu} lei')

    def salariuAnual(self):
        return print(f'Salariul meu anual este {self.salariu * 12} lei')

    def marireSalariu(self, marire):
        self.marire = marire
        return print(f'Salariul meu cu marire va fi {self.salariu + (self.marire / 100 * self.salariu)} lei')


p = Angajat('Ana', 'Alina', 2500)
p.descrie()
p.numeComplet()
p.salariuLunar()
p.salariuAnual()
p.marireSalariu(10)

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
print('Ex 2.')


class Factura:
    serie = 34502

    def __init__(self, numar, numeProdus, cantitate, pretBucata):
        self.numar = numar
        self.numeProdus = numeProdus
        self.cantitate = cantitate
        self.pretBucata = pretBucata

    def schimbaCantitate(self, nouaCantitate):
        self.cantitate = nouaCantitate

    def schimbaPretul(self, pret):
        self.pretBucata = pret

    def schimbaNumeProdus(self, nume):
        self.numeProdus = nume

    def genereazaFactura(self):
        import datetime
        print(f'Factura numarul {self.numar}, seria {self.serie}')
        print(f'Data:{datetime.datetime.now()}')
        from tabulate import tabulate
        print(tabulate([[str(self.numeProdus),
                        str(self.cantitate),
                        str(self.pretBucata),
                        str((self.cantitate * self.pretBucata))]],headers = ['Produs', 'Cantitate', 'Pret bucata', 'Total']))


f = Factura(6, 'Laptop', 6, 300)
f.schimbaCantitate(7)
f.schimbaPretul(700)
f.schimbaNumeProdus('Telefon')
f.genereazaFactura()
