'''
Folosim Simple Books API, descris aici :
https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md

Toata rezolvarea se va face într-o clasa numita Books API Client. Pentru testare se va crea un obiect din aceasta
clasa și se vor apela metodele implementate.

1. Folosind endpoint-ul de authentication, genereaza un access token (fa asta in constructor, client name si email
ar trebui sa fie atribute).

2. Adaugă o metoda prin care poți vedea toate comenzile.

3. Adaugă o metoda prin care poți vedea toate cărțile.

4. Adaugă o metoda prin care poți posta o comanda.

5. Adaugă o metoda prin care poți șterge o comanda.
'''

import requests
from pprint import pprint

'''
1. Folosind endpoint-ul de authentication, genereaza un access token (fa asta in constructor, client name si email
ar trebui sa fie atribute).
'''


class BooksAPIClient:
    def __init__(self, client, email):
        self.client = client
        self.email = email
        self.token = self._generate_token()

    def _generate_token(self):
        payload = {
            'clientName': self.client,
            'clientEmail': self.email
        }
        response = requests.post(url='https://simple-books-api.glitch.me/api-clients/', json=payload)
        print(response.json())
        return response.json()['accessToken']

    '''
    2. Adaugă o metoda prin care poți vedea toate comenzile.
    '''

    def view_all_orders(self):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.get('https://simple-books-api.glitch.me/orders', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    '''
    3. Adaugă o metoda prin care poți vedea toate cărțile.
    '''

    def view_all_books(self):
        response = requests.get('https://simple-books-api.glitch.me/books')
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    '''
    4. Adaugă o metoda prin care poți posta o comanda.
    '''

    def post_order(self, bookId, customer):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }  # specifica tipul de continut ca fiind json

        payload = {
            'bookId': bookId,
            'customerName': customer
        }
        response = requests.post(url='https://simple-books-api.glitch.me/orders', json=payload, headers=headers)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

    '''
    5. Adaugă o metoda prin care poți șterge o comanda.
    '''

    def delete_order(self, orderId):
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.delete(url=f'https://simple-books-api.glitch.me/orders/{orderId}', headers=headers)
        if response.status_code == 204:
            return 'Order deleted successfully'
        else:
            response.raise_for_status()


print('Ex 2.')
user = BooksAPIClient('user', 'user11@example.com')
print(user.view_all_orders())
print('Ex 3.')
all_books = user.view_all_books()
pprint(all_books)
print('Ex 4.')
pprint(user.post_order(bookId=1, customer="user"))
print('Ex 5.')
pprint(user.delete_order(orderId='MTDvH7q1SwiDVCZ7nhN0H'))
