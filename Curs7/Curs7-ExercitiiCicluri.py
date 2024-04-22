# CICLURI REPETITIVE

"""
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
‘Mașina mea preferată este x’.
Fă același lucru cu un for each.
Fă același lucru cu un while.
"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

print('EXERCITIUL 1 - cu FOR ')
# FOR - iteram peste indicii listei
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}')

print('EXERCITIUL 1 - cu FOR - EACH ')
# FOR EACH  - itereaza direct peste elementele listei
for i in masini:
    print(f'Masina mea preferata este {i}')

print('EXERCITIUL 1 - cu WHILE ')
# WHILE
i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1  # incrementeaza indexul cu 1 la sfarsitul fiecarei iterarii

'''
2. Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
'''
print('EXERCITIUL 2 - var 1.')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    if i == 0 or i == (len(masini) - 1):
        continue
    else:
        masini[i] = masini[i].upper()
else:
    print(f'Lista este {masini}')

# varianta 2
print('EXERCITIUL 2 - var 2.')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    if i != 0 and i != len(masini) - 1:
        masini[i] = masini[i].upper()
else:
    print(f'Lista este {masini}')

# Daca dorim audi si opel cu litere mici
# varianta 3
print('EXERCITIUL 2 - var 3.')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(len(masini)):
    if i == 0 or i == 8:
        masini[i] = masini[i].lower()
    elif i >= 1 or i < 8:
        masini[i] = masini[i].upper()
else:
    print(f'Lista este {masini}')

# varianta 4 - cu enumerate
print('EXERCITIUL 2 - var 4.')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for index, elem in enumerate(masini):
    print(index, elem)
    # functia enumerate este folosita pt a obtine atat indexul cat si valoarea fiecarui element din lista
    if index == 0 or index == len(masini) - 1:
        masini[index] = elem.lower()
    else:
        masini[index] = elem.upper()
else:
    print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
'''
print('EXERCITIUL 3 - var 1.')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Mercedes':
        print(f'Am gasit msina dumneavoastra')
        break
    else:
        print(f'Am gasit masina {i} . Mai cautam')

# varianta 2 - o alta idee
print('EXERCITIUL 3 - var 2.')
masina = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
client = input('Introduceti marca masinii: ')
for i in masina:
    if i == client == 'Mercedes':
        print(f'Am gasit masina dorita de dvs: {i}')
        break
    elif client not in masina:
        print(f'{client} nu face parte din oferta noastra')
        break
else:
    print(f'Am gasit masina {client}. Mai cautam.')

'''
4. Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 
Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
'''
print('EXERCITIUL 4')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Trabant' or i == 'Lăstun':
        continue
    print(f'S-ar putea sa va placa masina {i}')

'''
5.Modernizează parcul de mașini:
- Crează o listă goală, masini_vechi.
- Iterează prin mașini.
- Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
- Printează Modele vechi: x.
- Modele noi: x.
'''
print('EXERCITIUL 5 - var 1')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in masini:
    if i == 'Lăstun' or i == 'Trabant':
        masini_vechi.append(i)
        masini.remove(i)
print(f'Modele vechi {masini_vechi}')
masini.append('Tesla')
print(f'Modele noi {masini}')

# varianta 2 - cu enumerate
print('EXERCITIUL 5 - var 2')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for index, masina in enumerate(masini):
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini[index] = 'Tesla'
        masini = list(set(masini))
print(f'Modele vechi {masini_vechi}')
print(f'Masini existente plus plus Tesla {masini}')
'''
6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
- Prezintă doar mașinile care se încadrează în acest buget.
- Iterează prin dict.items() și accesează mașina și prețul.
- Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
- Iterează prin listă.
'''
print('EXERCITIUL 6')
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for masina,pret in pret_masini.items():
    if pret <= 15000:
        print(f'Masina {masina} are pretul {pret}')
        print(f'Pentru un buget de 15000 euro puteti alege masina {masina}')

'''
7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
- Iterează prin ea.
- Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
print('EXERCITIUL 7')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for i in numere:
    if i == 3:
        count += 1
print(f' 3 apare in lista de {count} ori')

'''
8. Aceeași listă:
- Iterează prin ea
- Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
print('EXERCITIUL 8')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in numere:
    suma += i
print(f'Suma este {suma}')

'''
9. Aceeași listă:
- Iterează prin ea.
- Afișază cel mai mare număr (nu ai voie să folosești max).
'''
print('EXERCITIUL 9')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = 0
for i in numere:
    if i > maxim:
        maxim = i
print(f'Cel mai mare numar din lista este {maxim}')

'''
10. Aceeași listă:
- Iterează prin ea.
- Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
- Afișază noua listă.
'''
print('EXERCITIUL 10')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
noua_lista = []
for i in numere:
    if i < 0 :
        noua_lista.append(-i)
    else:
        noua_lista.append(i)
print(noua_lista)

'''
11. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
- Itereaza prin listă alte_numere 
- Populează corect celelalte liste
- Afișează cele 4 liste la final
'''
print('EXERCITIUL 11 - var 1 ')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    if i % 2 == 1:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    if i < 0:
        numere_negative.append(i)
print(f'Lista numerelor pare este {numere_pare}')
print(f'Lista numerelor impare este {numere_impare}')
print(f'Lista numerelor pozitive este {numere_pozitive}')
print(f'Lista numerelor negative este {numere_negative}')

print('EXERCITIUL 11 - var 2 ')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
numar_neutru = []
for i in alte_numere:
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i > 0:
        numere_pozitive.append(i)
    elif i == 0 :
        numar_neutru.append(i)
    else:
        numere_negative.append(i)
print(f'Lista numerelor pare este {numere_pare}')
print(f'Lista numerelor impare este {numere_impare}')
print(f'Lista numerelor pozitive este {numere_pozitive}')
print(f'Lista numerelor negative este {numere_negative}')

'''
12. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
'''
print('EXERCITIUL 12 - var 1. ')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
print(alte_numere)

print('EXERCITIUL 12 - var 2. - Bubble Sort')
numere_bubble = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
sorted = False
while not sorted:
    # setam sorted ca si True la inceputul fiecarui ciclu si asta presupune ca lista noastra este sortata
    # daca se gasesc doua elemente care trebuie interschimbate , sorted va fi setat ca si false
    sorted = True
    # iteram printr-o bucla For pentru a parcurge elementele listei iar range(len(numere_buble)-1) asigura
    # ca parcurgem lista pana la penultimul element
    for i in range(len(numere_bubble) - 1):
        if numere_bubble[i]>numere_bubble[i+1] :
            numere_bubble[i],numere_bubble[i+1]=numere_bubble[i+1],numere_bubble[i] # inteschimbam prin asignare multipla
            sorted = False # indica faptul ca lista nu este sorata compelt iar bucla while trebuie sa continue
print(numere_bubble)