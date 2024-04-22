'''
4. Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number (e.g. 1st, 2nd, 3rd, etc.)
'''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for index,element in enumerate(alphabet): # am luat indexul si am enumerat prin alfabet
    with open(f'{element}.txt','w') as f: # luam fieacre litera din alf., elementul il inlocuim cu litera si formam fisierul
        f.write(f'My name is letter {element}\n')
        sufix = ''
        if index == 0 or index == 20:
            sufix = "'st"
        elif index == 1 or index == 21:
            sufix = "'nd"
        elif index == 2 or index == 22:
            sufix == "'rd"
        else:
            sufix = "'th"

        f.write(f'I am the {index+1}{sufix} letter of the alphabet')