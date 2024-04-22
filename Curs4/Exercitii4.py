#Exercitii echipa 4

'''
1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o. Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
'''
print('EXERCITIUL 1')
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
inversare1 = note_muzicale[::-1]
print(inversare1)
inversare1.reverse()
print(inversare1)

#2.De cate ori apare 'do'?
print('EXERCITIUL 2')
aparitie = note_muzicale.count('do')
print(aparitie)

#3.Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua
print('EXERCITIUL 3')
tup = tuple(note_muzicale)
print(type(tup))
#Nu CRED ca se poate

#4.Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata de cate ori
# apare nota in gama. Afiseaza-l.
print('EXERCITIUL 4')
note_muzica = {
    'do' : 2,
    're' : 1,
    'mi' : 1,
    'fa' : 1,
    'sol' : 1,
    'la' : 1,
    'si' :1,
}
print(note_muzica)

#sau

note_dict = {
    'do' :note_muzicale.count('do'),
    're' : note_muzicale.count('re'),
    'mi' : note_muzicale.count('mi'),
    'fa' : note_muzicale.count('fa'),
    'sol' :note_muzicale.count('sol'),
    'la' : note_muzicale.count('la'),
    'si' :note_muzicale.count('si'),
}
print(note_dict)