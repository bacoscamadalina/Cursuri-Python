'''
                                    CERINTE MINIPROIECT -B-

CLASA: TodoList
    Atribute: Todo ( dict ; cheia e numele taskului ; valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor

     Metode:
- adauga_task(nume, descriere) - se va adauga in dict
- finalizează_task(nume) - se va sterge din dict
- afișează_todo_list() - doar cheile
- afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
    * Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
    * Dacă acesta răspunde nu - la revedere
    * Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict
'''


class TodoList:
    def __init__(self):
        self.todo = {}

    def adaugaTask(self, nume, descriere):
        self.todo[nume] = descriere   # construim dictionarul

    def finalizeazaTask(self, nume):
        if nume in self.todo:  # verifica daca task-ul este in dict, iar daca exista, il va sterge
            del self.todo[nume]
        else:
            print('Task-ul nu exista in lista')

    def afișează_todo_list(self):
        for nume in self.todo.keys():  # itereaza prin cheile dict si afiseaza valorile
            print(nume)

    def afișează_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo:
            print(f'Detalii pentru nume task: {nume_task} : {self.todo[nume_task]} ')
        else:
            raspuns = input(f'Task-ul {nume_task} nu exista. Doriti sa-l adaugati? (Da/Nu)')
            if raspuns.lower() == 'da':
                descriere = input('Introduceti detalii pentru task.')
                self.adaugaTask(nume_task,descriere)
            else:
                print('Bye,bye')

todolist = TodoList()
todolist.adaugaTask('Cumparaturi','lapte,paine,oua')
todolist.afișează_todo_list()
todolist.adaugaTask('Plata facturi','gaz,curent,apa')
todolist.afișează_todo_list()
todolist.afișează_detalii_suplimentare('Cumparaturi')

'''
todolist.afișează_detalii_suplimentare('Vanzare')
todolist.afișează_detalii_suplimentare('Vanzare')
'''

todolist.finalizeazaTask('Cumparaturi')
todolist.finalizeazaTask('Plata facturi')
todolist.afișează_todo_list()