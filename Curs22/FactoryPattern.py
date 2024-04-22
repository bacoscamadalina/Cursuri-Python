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

from abc import ABC, abstractmethod


class TranslatorInterface(ABC):
    @staticmethod
    @abstractmethod
    def localize(word):
        pass


class EnglishTranslator(TranslatorInterface):
    translations = {'masina': 'car',
                    'casa': 'house',
                    'barbat': 'man',
                    'femeie': 'woman'
                    }

    @staticmethod  # poate fi apelata direct pe clasa, fara a crea o instanta
    def localize(word):
        return EnglishTranslator.translations.get(word, word)


class FrenchTranslator(TranslatorInterface):
    translations = {'masina': 'voiture',
                    'casa': 'maison',
                    'barbat': 'homme',
                    'femeie': 'femme'
                    }

    @staticmethod  # poate fi apelata direct pe clasa, fara a crea o instanta
    def localize(word):
        return FrenchTranslator.translations.get(word, word)


class SpanishTranslator(TranslatorInterface):
    translations = {'masina': 'auto',
                    'casa': 'casa',
                    'barbat': 'hombre',
                    'femeie': 'mujer'
                    }

    @staticmethod  # poate fi apelata direct pe clasa, fara a crea o instanta
    def localize(word):
        return SpanishTranslator.translations.get(word, word)


print(f'In engleza zicem {EnglishTranslator.localize("masina")}')
print(f'In spaniola zicem {SpanishTranslator.localize("masina")}')
print(f'In franceza zicem {FrenchTranslator.localize("masina")}')
print(f'In franceza zicem {FrenchTranslator.localize("usa")}')

