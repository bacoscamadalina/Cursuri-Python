#                                 Context Managers ca o Clasa


'''
CONTEXT MANAG = utilizat pt gestionarea resurselor care necesita deschiderea si inchiderea explicita
              -> folosit ca sa seteze un context inainte de executia unui bloc de corsi sa faca curatenie dupa
Metode speciale : __enter__()
                  __exit__()
'''

print('EX 1.')
#


class HelloContextManager():
    def __enter__(self):  # metoda speciala care se executa atunci cand se intra in blocul "with"
        print('Intram in context')
        return 'Hello Word!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        :param exc_type: este tipul exceptiei(clasa exceptie care s-a ridicat in blocul with)
        :param exc_val: valoarea sau instanta exceptiei (daca nu a avut loc o exceptie va fi NONE)
        :param exc_tb: este traceback-ul exceptiei (info unde exceptia a fost ridicata)
        '''
        print('Iesim din context')
        # aici se pot adauga actiuni suplimentare pentru gestionarea exceptiilor


with HelloContextManager() as h:  # variabila "h" va lua valoarea returnata de metoda __enter__() (adica HelloWord)
    print(h)

print('Nu mai suntem in context')

print('EX 2.')


class HelloContextManager:
    def __enter__(self):
        print('Intram in context')
        return 'Hello Word!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Iesim din cotext')
        if exc_type == IndexError:
            print(f'Mesaj de eroare : {exc_val}')
            return True  # daca punem 'FALSE', nu se mai trateaza eroarea si astfel introducem eroarea in cod


with HelloContextManager() as h:
    print(h)
    h[100]  # 100 rep nr de caractere
print('Nu mai sunt in context')
