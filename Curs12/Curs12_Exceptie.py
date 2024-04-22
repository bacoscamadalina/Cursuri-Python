# CUM RIDICAM O EXCEPTIE?


class CustomException(Exception):
    pass


'''
Sa se scrie o functie care verifica daca o lista de nr. intregi contine nr. negative. Daca da, sa se arunce o exceptie 
specifica. 
'''


class ContainsNegativeNumberException(Exception):
    pass  # aceasta este eroarea pe care dorim sa o aruncam


# functia care verifica daca avem numere negative
def checkNegativeNumbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativeNumberException(f'Contine numerul negativ {number}')


checkNegativeNumbers([1, 2, 3, -1, -2, -3])  # contine doar -1 deoarece s-a oprit for-ul
