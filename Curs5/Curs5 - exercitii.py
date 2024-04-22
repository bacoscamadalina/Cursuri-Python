# 3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4] .Găsește 2 variante să le unești într-o singură listă
print("EXERCITIUL 3")
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
# varianta 1
unire = lista1 + lista2
print(unire)

# varianta 2
extins = lista1.extend(lista2)
print(lista1)

# varianta 3 (lista1.append(lista2))

'''
4.
Sortează și afișează lista generată la exercițiul anterior.
Elimina numărul 0 folosind o funcție.
Afișaza iar lista.
'''
print("EXERCITIUL 4")
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
unire = lista1 + lista2
unire.sort()
print(unire)
unire.remove(0)  # sau unire.pop(0 - item)
print(unire)

'''
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
'''
print("EXERCITIUL 5")
# varianta 1
if unire is None:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# varianta 2
if len(unire) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# varianta 3
if unire == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# varianta 4
if not unire:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
print("EXERCITIUL 6")
elimina = unire.clear()
print(unire)
# sau cu " del unire "

# 7. Copy paste la exercițiul 5. Verifică încă o dată. Acum ar trebui să se afișeze că lista e goală.
print("EXERCITIUL 7")
# varianta 1
if elimina is None:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# varianta 2
if len(unire) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# varianta 3
if unire == []:
    print('Lista este goala')
else:
    print('Lista nu este goala')

# varianta 4
if not unire:
    print('Lista este goala')
else:
    print('Lista nu este goala')

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
print("EXERCITIUL 8")
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
print(list(dict1.keys()))  # am facut o lista sa dispara dict_keys

'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
print("EXERCITIUL 9")
# varianta 1
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
nume = input("Introdu un nume: ")
print(f'{nume} a luat nota {dict1[nume]} ')

# varianta 2 - daca introducem un nume inexistent in dictionar
nume = input("Introdu un nume: ")
nota = dict1.get(nume)
if nota is None:
    print('Ai introdus un nume incorect')
else:
    print(f'{nume} a luat nota {dict1[nume]} ')

'''
10 . Dorel a făcut contestație și a primit 6
- Modifică nota lui Dorel în 6
- Printează nota după modificare
'''
print("EXERCITIUL 10")
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 6}
print(dict1)

'''
11. Gigel se transferă din clasă
- Căuta o funcție care să îl șteargă
- Vine un coleg nou. Adaugă Ionică, cu nota 9
- Printează noii elevi
'''
print("EXERCITIUL 11")
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1.pop('Gigel')
print(dict1)
dict1['Ionica'] = 9
print(dict1)

'''
13. Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
- Adaugă în zilele_sapt ‘luni’
- Afișează zile_sapt
'''
print("EXERCITIUL 13")
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

'''
14. Folosește un if și verifică dacă:
- Weekend este un subset al zilelor din săptămânii.
- Weekend nu este un subset al zilelor din săptămânii.
'''
print("EXERCITIUL 14")
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii')
else:
    print('Weekend nu este un subset al zilelor din săptămânii')

# 15. Afișează diferențele dintre aceste 2 seturi.
print("EXERCITIUL 15")

# varianta 1
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
diferenta1 = zile_sapt.difference(weekend)
print(diferenta1)
# varianta 2
diferenta2 = zile_sapt - weekend
print(diferenta2)

# 16. Afișează intersecția elementelor din aceste 2 seturi.
print("EXERCITIUL 16")
intersectia = zile_sapt.intersection(weekend)
print(intersectia)

# varinta 2
intersectia2 = zile_sapt and weekend
print(intersectia2)
