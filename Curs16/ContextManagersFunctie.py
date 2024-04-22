#                                 Context Managers ca o functie
from contextlib import contextmanager


@contextmanager
def helloContextManager():
    # pana aici avem echivalent cu metoda __enter__()
    print('Intram in context')
    # controlul trece in modul "with"
    yield 'Hello Word'
    # echivalent cu metoda __exit__()
    print('Iesim din context')


with helloContextManager() as h:
    print(h)
