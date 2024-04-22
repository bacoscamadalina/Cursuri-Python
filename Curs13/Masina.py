'''
                                   CERINTE MINIPROIECT -A-

CLASA : MASINA
Atribute: marca, model, viteza maximă, viteza_actuală, culoare, culori disponibile (set), înmatriculată (bool)
   Culoare = gri - toate mașinile când ies din fabrică sunt gri
   Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrică
   Culori disponibile = alege tu 5-7 culori
   Marca = alege tu - fabrica produce o singură marcă, dar mai multe modele
   Înmatriculată = False
Constructor: model, viteza_maxima
Metode:
- descrie() - se vor printa toate atributele, în afară de culori_disponibile
- înmatriculare() - va schimba atributul înmatriculată în True
- vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua culoare e în opțiunea de culori disponibile,
altfel afișați o eroare
- accelerează(viteza) - se va accelera la o anumită viteză, dacă viteza e negativă-eroare,
dacă viteza e mai mare decât viteza_max - masina va accelera până la viteza maximă
- franeaza() - mașina se va opri și va avea viteza 0
'''


class Masina:
    culoare = {'Gri', 'Verde', 'Rosu'}
    marca = 'Audi'

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'Gri'
        self.inmatriculat = False

    def descriere(self):
        print(
            f'Marca : {self.marca} , model : {self.model}, viteza maxima : {self.viteza_maxima}, viteza actuala: {self.viteza_actuala}, '
            f'culoare: {self.culoare}')

    def inmatriculare(self):
        self.inmatriculat = True

    def vopseste(self, culoare):
        if culoare in Masina.culoare:
            self.culoare = culoare
        else:
            print('Eroare. Culoarea selectata nu este disponibila')

    def accelerează(self, viteza):
        if viteza < 0:
            print('Eroare! Viteza nu poate fi negativa')
        else:
            self.viteza_actuala = min(viteza, self.viteza_maxima)

    def franeaza(self):
        self.viteza_actuala = 0


class MasinaSport(Masina):
    def __init__(self, model, viteza_maxima):
        super().__init__(model, viteza_maxima)
        self.viteza_maxima += 50

    def accelereaza(self, viteza):  # polimorf
        if viteza < 0:
            print('Eroare! Viteza nu poate fi negativa')

        elif viteza > self.viteza_maxima:
            print(f'Viteza maxima atinsa : {self.viteza_maxima} km/h')
        else:
            print(f'Accelerare la {viteza} km/h')
            self.viteza_actuala = viteza

masina = Masina('A3',200)
masina.descriere()
masina.vopseste('Rosu')
masina.descriere()
masina.vopseste('Roz')
masina.descriere()

masina2 = MasinaSport('A6',220)
masina2.descriere()
masina2.accelereaza(240)
