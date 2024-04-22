'''
3. Declara un string care contine toate literele alfabetului. Folosind functia enumerate, care primește ca si parametru
o colecție (lista, tupla, string) si returnează un iterator, afișează pentru fiecare litera în parte:
`Pe mine ma cheama X si sunt a n-a litera din alfabet`
Nu uite sa gestionezi cazurile speciale (prima litera, etc)
'''
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for index,element in enumerate(alfabet):
    sufix = ''
    if index == 0:
        sufix = 'prima'
        print(f'Pe mine mă cheamă {element} si sunt {sufix} litera din alfabet ')
    else:
        sufix = '-a'
        print(f'Pe mine mă cheamă {element} si sunt a {index+1}{sufix} litera din alfabet ')