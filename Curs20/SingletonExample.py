'''
                                  SINGLETON

- sablon creational care se asigura ca o clasa are doar o singura instanta si asigura acces operational catre aceasta
instanta

AVANTAJE :
- poti fi sigur ca o clas are o singura instanta
- acea instanta este accesibila de oriune din cod
- acea instanta este initializata doar cand este folosita pentru prima oara
DEZAVANTAJE:
- acest sablon poate masca un design slab (ex: atunci cand componentele programului stiu prea multe una despre cealalta)


'''

print('--Prima incercare--')


class SingletonLogger:
    def __init__(self, filename):
        self.filename = filename


# facem doua instante
logger = SingletonLogger('hello.txt')
logger2 = SingletonLogger('hello2.txt')

print(logger)
print(logger2)

print('--A doua incercare--')


class SingletonLogger:
    # introducem un atribut de clasa
    _instance = None

    # definim o metoda speciala (__new__)
    def __new__(cls, *args,
                **kwargs):  # metoda speciala apelata inainte de init care controleaza crearea noilor instante ale clasei

        # new este locul in care ne asiguram ca doar o singură instanta a clasei este creata
        if cls._instance is None:
            print('Create object')
            cls._instance = super().__new__(
                cls)  # apelam mai departe functia speciala new pe care am suprascris-o ca sa adaugam comportamentul extra
        return cls._instance

    def __init__(self, filename):
        self.filename = filename


# facem doua instante
logger = SingletonLogger('hello.txt')
logger2 = SingletonLogger('hello2.txt')

print(logger)
print(logger2)

print(logger.filename)
print(logger2.filename)

print('--A treia varianta--')


class SingletonLogger:
    # introducem un atribut de clasa
    _instance = None

    # definim o metoda speciala (__new__)
    def __new__(cls, *args,
                **kwargs):  # metoda speciala apelata inainte de init care controleaza crearea noilor instante ale clasei

        # new este locul in care ne asiguram ca doar o singură instanta a clasei este creata
        if cls._instance is None:
            print('Create object')
            cls._instance = super().__new__(
                cls)  # apelam mai departe functia speciala new pe care am suprascris-o ca sa adaugam comportamentul extra
        return cls._instance

    def __init__(self, filename):
        if not hasattr(self,'filename'): # utilizam aceasta functie in __init pt a verifica daca atributul filename a fost deja setat
            self.filename = filename


# facem doua instante
logger = SingletonLogger('hello.txt')
logger2 = SingletonLogger('hello2.txt')

print(logger)
print(logger2)

print(logger.filename)
print(logger2.filename)
