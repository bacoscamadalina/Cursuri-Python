'''
Acest pattern ne permite sa creăm un obiect dintr-o clasa folosind o alta clasa (fabrica). Fabrica are posibilitatea
de a crea obiecte din mai multe clase (de obicei aceste clase sunt siblings, adica mostenesc de la acelasi parinte).

Vom implementa următoarele clase:
English/French/Spanish Translator – clase care știu sa traduca cuvinte din română în limba specificata
translations va fi un dicționar cu acele cuvinte, exemplu `{ “masina”: “car” }` – se poate hardcoda în clasa
localize va fi o funcție care pentru un parametru de intrare, ne va da traducerea lui în acea limba (exemplu
`input(“masina”)` returneaza “car”)

TranslatorFactory – clasa care are o singura metoda (preferabil statica sau de clasa) numita get_translator(language) –
in functie de parametrul language, returnează un translator object.


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
'''


class BaseTranslator:
    def __init__(self, translations):
        self.translations = translations

    def localize(self, word):
        return self.translations.get(word, 'Translation not available')


class EnglishTranslator(BaseTranslator):
    def __init__(self):
        super().__init__({'masina': 'car',
                          'casa': 'house',
                          'barbat': 'man',
                          'femeie': 'woman'
                          })


class FrenchTranslator(BaseTranslator):
    def __init__(self):
        super().__init__({'masina': 'voiture',
                          'casa': 'maison',
                          'barbat': 'homme',
                          'femeie': 'femme'
                          })


class SpanishTranslator(BaseTranslator):
    def __init__(self):
        super().__init__({'masina': 'auto',
                          'casa': 'casa',
                          'barbat': 'hombre',
                          'femeie': 'mujer'
                          })

# clasa pentru crearea traducerilor in functie de codul de limba dat(en,fr,es)
class TranslatorFactory:
    @classmethod     # metoda de clasa pt a obtine o instanta a traducatorului corespunzator limbii specificate
    def get_translator(cls,language):
        if language == 'en' :
            return EnglishTranslator()
        elif language == 'fr':
            return  FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator()
        else:
            return ValueError('Invalid language code')

english_trans = TranslatorFactory.get_translator('en')
french_trans = TranslatorFactory.get_translator('fr')
spanish_trans = TranslatorFactory.get_translator('es')

print(f'In engleza zicem: {english_trans.localize("masina")}')
print(f'In spaniola zicem: {spanish_trans.localize("masina")}')
print(f'In franceza zicem: {french_trans.localize("masina")}')
print(f'In franceza zicem: {french_trans.localize("usa")}')


