# SERIALIZAREA DATELOR - citirea datelor din fisiere
# Construim o functie care citeste fisierul nr text si il afișează in consola:
def read(filename):
    with open(filename, 'r') as f:  # deschide fisierul in modul read si stocheaza obiectul in variabila f
        return f.readlines()  # citeste linie cu linie din fisier


print(read('numere.txt'))


# Construim o functie de scriere
def write(filename, data):
    with open(filename, 'w') as f:  # deschide fisierul in modul scriere
        f.writelines(data)


write('numere2.txt', ['1' '2' '3' '4'])
write('numer2.txt', ['1\n' '2\n' '3\n' '4\n'])


# Ca sa scriem in continuare ce dorim sa scriem in fisier ne folosim de functia 'append' (adaugare)
def append(filename, data):
    with open(filename, 'a') as f:
        f.writelines(data)


append('numer2.txt', ['1\n' '2\n' '3\n' '4\n'])
