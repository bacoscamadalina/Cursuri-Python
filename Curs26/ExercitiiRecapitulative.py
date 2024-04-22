'''
1. Creaza o functie Python care inversează și returnează un număr întreg pozitiv. În cazul unui număr negativ,
afișează o eroare.
Exemple:
reverse(1234567) => 7654321
reverse(10) => 1
reverse(101) => 101
reverse(10000000) => 1
reverse(-65) => eroare
'''

print('Ex. 1')

def inversare(numar):
    numar_inversat = 0
    if numar > 0:
        while numar != 0:
            ultima_cifra = numar % 10
            numar_inversat = numar_inversat * 10 + ultima_cifra
            numar //= 10  # eliminam ultima cifra
        print(f'Numarul inversat este: {str(numar_inversat)} ')
    else:
        print('Avem o eroare. Numarul este negativ')


inversare(12345)


# sau

def inversat(numar):
    if numar > 0:
        numar_inversat = str(numar)[::-1]
        print(f'Numaru inversat este {numar_inversat}')
    else:
        print('Avem o eroare. Numarul este negativ')

inversat(12345)



'''
2. Creaza o functie Python care primește o lista și un număr întreg pozitiv k, si roteste lista cu k pozitii. 
Exemple:
rotate([1, 2, 3, 4, 5], 2) => [3, 4, 5, 1, 2]
rotate([1, 2, 3, 4, 5], 4) => [5, 1, 2, 3, 4]
rotate([1, 2, 3, 4, 5], 8) => [4, 5, 1, 2, 3]
'''
print('Ex. 2')


def rotire(lista,numar):
    rotire = lista[numar:] +lista[:numar]
    print(rotire)



rotire([1,2,3,4,5],2)

'''
3. Creaza o functie Python care primește 2 stringuri, și verifica dacă acestea sunt anagrame (case-insensitive).
Exemple:
is_anagram(‘Adela’, ‘ealad’) => True
is_anagram(‘ITFactory’, ‘acfiorty’) => True
is_anagram(‘Stringy’, ‘gringsty’) => False
is_anagram(‘ana’, ‘ioana’) => False
'''
print('Ex. 3')


def is_anagram(cuvant1,cuvant2):
    if sorted(cuvant1.lower()) == sorted(cuvant2.lower()):
        print(f"Cuvantul {cuvant1} si cuvantul {cuvant2} sunt anagrame")
    else:
        print(f"Cuvantul {cuvant1} si cuvantul {cuvant2} nu sunt anagrame")


is_anagram('Adela', 'ealad')
is_anagram('ITFactory', 'acfiorty')
is_anagram('Stringy', 'gringsty')
is_anagram('ana', 'ioana')


'''
4.Creaza o functie Python care primeste o lista de numere, si il returneaza pe al doilea cel mai mare numar distinct.
Exemple:
get_second_biggest([1,2,3,4,5]) => 4
get_second_biggest([1,2,3,4,4]) => 3
get_second_biggest([1,2,4,4,4]) => 2
get_second_biggest([-1,-2,-3,-4,-5]) => -2
'''
print('Ex. 4')
def get_second_biggest(lista):
    lista_noua = set(lista)
    maxim = max(lista_noua)
    lista_noua.remove(maxim)
    print(max(lista_noua))


get_second_biggest([1,2,3,4,5])
get_second_biggest([1,2,3,4,4])
get_second_biggest([1,2,4,4,4])
get_second_biggest([-1,-2,-3,-4,-5])



'''
5. Creaza o functie Python care primeste doua stringuri ce reprezinta niste numere foarte mari, si returneaza rezultatul
adunarii “numerelor”, tot sub format string:
Exemple:
add_two(‘12345’, ‘12345’) => ‘24690’
add_two(‘1234’, ‘4321’) => ‘5555’
add_two(‘563895634’, ‘548967348053’) => ‘549531243687’

'''
print('Ex. 5')
def add_two(n1,n2):
    suma = int(n1) + int(n2)
    print(f'Suma este : {str(suma)} ')

add_two('12345', '12345')
add_two('1234', '4321')
add_two('563895634', '548967348053')


'''
6. Creaza o functie Python care primeste un numar n, si o lista de numere de dimensiune n-1. In lista se afla toate 
numerele de la 1 la n, in afara de 1. Functia trebuie sa gaseasca acel numar in cel mai eficient mod posibil si sa-l 
returneze.
Exemple:
find_missing(5, [1,2,3,5]) => 4
find_missing(2, [1]) => 2
find_missing(7, [6,5,1,3,2,7]) => 4
'''
print('Ex. 6')
def find_missing(numar,lista):
    suma_totala = sum(range(1,numar+1))
    suma_lista = sum(lista)
    numar_lipsa = suma_totala-suma_lista
    print(f'Numarul lipsa este: {numar_lipsa}')


find_missing(5, [1,2,3,5])
find_missing(2, [1])
find_missing(7, [6,5,1,3,2,7])


'''
Creaza o clasa Calendar, care primeste ca unic parametru un an, si genereaza “calendarul” acelui an. Se va tine cont 
de faptul daca anul este bisect sau nu. Metode:
-> init(an) 
-> print_calendar(luna) - va printa calendarul pentru luna menționată intr-un format user-friendly, ex
October 2022
Mo 	Tu 	We 	Th 	Fr 	Sa 	Su
1 	2
3 	4 	5 	6 	7 	8 	9
10 	11 	12 	13 	14 	15 	16
17 	18 	19 	20 	21 	22 	23
24 	25 	26 	27 	28 	29 	30
31
	-> get_day_of_week(zi, luna) - va returna ce zi din saptamna este, exemplu ‘Marti’
-> get_days_in_month(luna) - va returna numarul de zile din luna respectivă;
'''
print('Ex. 7')

import calendar

class Calendar:

    def __init__(self,year):
        self.year = year


    def print_calendar(self,month):
        self.month = month
        print(calendar.month(self.year,self.month))


    def get_day_of_week(self,day,month):
        self.month = month
        self.day = day
        day_of_week = calendar.weekday(self.year,self.month,self.day)
        if day_of_week == 0 :
            print('MONDAY')
        elif day_of_week == 1:
            print('TUSDAY')
        elif day_of_week == 2:
            print('WEDNESDAY')
        elif day_of_week == 3:
            print('THURSTDAY')
        elif day_of_week == 4:
            print('FRIDAY')
        elif day_of_week == 5:
            print('SATURDAY')
        elif day_of_week == 6:
            print('SUNDAY')



    def get_days_in_month(self,month):
        self.month = month
        days_in_month = calendar.monthrange(self.year,self.month)
        print(f'The month has : {days_in_month} days')


c = Calendar(2024)
c.print_calendar(2)
c.get_day_of_week(1,2)
c.get_days_in_month(2)