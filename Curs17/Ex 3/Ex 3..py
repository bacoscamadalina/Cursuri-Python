'''
                                          - CONTEXT MANAGERS -
3. Se da un fisier text hello.txt, care contine un text scurt. Deschideți fișierul și citiți conținutul, folosind
următoarele 2 metode:
try - finally
Fișierul se deschide înainte de try, folosind funcția open
În interiorul try citim conținutul folosind funcția read
În finally se închide fișierul
with (context manager)
Se va observa ca pentru with nu mai este nevoie sa inchidem noi manual fișierul, pentru ca context managerul
face asta pentru noi.
'''
print('EX 3.')

with open('hello.txt','w') as file:
    file.write('HelloWord')

class Context:

    def __init__(self,file):
        self.file = file

    def __enter__(self):
        self.file = open(self.file,'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            content = self.file.read()
            print(content)
        finally:
            self.file.close()
            print('S-a inchis fisierul')


with Context('hello.txt') as h:
    content = h.read()
    print(content)

