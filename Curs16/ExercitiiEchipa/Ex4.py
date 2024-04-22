'''
4. Declara trei liste: una cu oameni, una cu salarii, si una cu meserii  (important: trebuie sa aiba acelasi număr de
elemente). Apoi foloseste functia zip, care primeste ca si parametru un numar de colectii si returneaza un iterator
pentru a afisa:
`Pe mine ma cheama X, sunt de profesie Y, si castig Z ron pe luna`
'''
oameni = ['Ana', 'Sorin', 'Andreea']
salarii = [3400, 5320, 4000]
meserii = ['Medic', 'Inginer', 'Dansatoare']


for persoana,bani,munca in zip(oameni,salarii,meserii):
    print(f'Pe mine mă cheama {persoana}, sunt de profesie {munca}, si castig {bani} ron pe luna.')