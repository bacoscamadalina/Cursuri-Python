'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

- Declară o Listă cu 5 jucători
- Schimbari_efectuate = te joci tu cu valori diferite
- Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișează a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
- Afișează ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
- Afișează ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
'''

echipa = ['A', 'B', 'C', 'D', 'E']
schimbari_efectuate = int(input('Introduceti numarul de schimbari : '))
jucator = input('Introduceti  numele jucatorului: ')
sch_max = 3
sch_min = 0
diferenta = sch_max - schimbari_efectuate
if jucator in echipa and sch_min < diferenta < sch_max:
    print(f'Jucatorul {jucator} este in teren si mai avem {diferenta} schimbari la dispozitie')
    print('Efectueaza schimbarea')
    jucator_sters = echipa.remove(jucator)
    print(f'Jucatorul {jucator} a fost sters')
    jucator_adaugat = input('Introduceti numele noului jucator: ')
    echipa.append(jucator_adaugat)
    print(f'A intrat {jucator_adaugat}, a iesit {jucator} si mai avem {diferenta} schimbari la dispozitie')
    if diferenta <= 0:
        print('Nu mai ai schimbari')
else:
    print(f'Nu se mai poate efectua schimbarea deoarece jucatorul {jucator} nu este in teren')
    print(f'Mai ai {diferenta}')



jucatori = ['Hagi', 'Marius', 'Andrei', 'lacatus', 'Dorel']
Schimbari_efectuate = int(input('numarul de schimbari'))
Schimbari_max = 3
dif_schimb = Schimbari_max - Schimbari_efectuate
rezerva = input(' numele rezervei:')

if f"Jucătorul din  {jucatori} e în teren și mai avem schimbări la dispoziție":
    print(f'efectuam schimbarea ')
    if f"stergem un jucator si adaugam unul din {rezerva}":
        jucator_1 = jucatori.pop(2)
        jucatori.append(rezerva)
    print(f'a intrat {rezerva}, a ieșit {jucator_1}, mai ai {dif_schimb} schimbări')
if f"jucatorul{jucator_1} nu e in teren":
    print(f'nu se poate efectua schimbarea deoarece jucătorul {jucator_1} nu e în teren')
else:
    print(f'mai ai {dif_schimb} schimbări')

    #varianta 3

    lista_jucatori = ["jucator_1", "jucator_2", "jucator_3", "jucator_4", "jucator_5", "jucator_6", ]
    schimbari_efectute = 2
    schimbari_maxime = 3

    schimb = input("Vrei sa faci o schimbare? (y/n)")

    if schimb == "y":
        jucator_scos = input("Introdu jucatorul pe care vrei sa il scoti: ")
        if jucator_scos not in lista_jucatori:
            print(f"Nu se poate efectua schimbarea. Jucatorul {jucator_scos} nu exista in teren \n"
                  f"Mai ai {schimbari_maxime - schimbari_efectute} schimbari")
        else:
            lista_jucatori.remove(jucator_scos)
            jucator_adaugat = input("Introdu jucatorul pe care vrei sa il adaugi: ")
            lista_jucatori.extend(jucator_adaugat)
            print(f"A iesit jucatorul {jucator_scos} si a intrat {jucator_adaugat} \n"
                  f"Mai ai {schimbari_maxime - schimbari_efectute} schimbari")