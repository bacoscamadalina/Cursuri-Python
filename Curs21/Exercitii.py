'''
Folosim https://jsonplaceholder.typicode.com/guide/ Toate requesturile se vor face prima data in Postman
(pentru verificare), iar apoi folosind libraria requests din Python.

Structura datelor este următoarea:
- fiecare post este deținut de un user, și poate avea mai multe comments
- fiecare album este deținut de un user, și poate avea mai multe photos
- fiecare todo este detinut de un user.

1. Alege un user din lista de useri predefiniti. Pentru acesta, fa requesturile necesare pentru a afișa următoarele
informații:
	-> lista de posts
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații
despre primele 3 obiecte, iar apoi afiseaza "+x more posts/", unde x este numărul de obiecte rămase.
'''
import requests
from pprint import pprint


class PostAPIClient:
    URL = 'https://jsonplaceholder.typicode.com/'

    def get_post_by_user(self, userId):
        response = requests.get(f'{self.URL}/posts?userId = {userId} ')
        post = response.json()
        '''
        Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații
        despre primele 3 obiecte, iar apoi afiseaza "+x more posts/", unde x este numărul de obiecte rămase.
        '''
        first_three = post[:3]
        return first_three, len(post) - 3

    '''
    2. Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.
    '''

    def get_comments_by_post(self, post_id):
        response = requests.get(f'{self.URL}/comments?post_id = {post_id}')
        return response.json()

    def get_album_by_post(self, albumId):
        response = requests.get(f'{self.URL}/photos?albumId = {albumId}')
        return response.json()

    '''
    3. Creeaza un post nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea cum ar arata în 
    viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
    '''

    def create_post(self, new_post):
        response = requests.post(f'{self.URL}/posts', json=new_post)
        return response.json()

    '''
    5. Folosind query parameters, filtrează lista de todos pentru userul ales astfel incat sa afisezi doar todos care 
    nu sunt completed.
    '''
    def get_todo_by_user(self,userId):
        response = requests.get(f'{self.URL}todos?userId={userId}&completed=false')
        return response.json()


print('Ex 1.')
client = PostAPIClient()
post, left = client.get_post_by_user(1)
pprint(post)
print(f'+{left} more posts')
print('Ex 2.')
pprint(client.get_comments_by_post(1))
pprint(client.get_album_by_post(1))
print('Ex 3.')
payload = {
    'body': 'postare noua',
    'title': 'titlu nou',
    'userId': '2',
    'id' : '102'
}
pprint(client.create_post(payload))
print('Ex 5.')
pprint(client.get_todo_by_user(1))

'''
4. Alege un post existent și realizează operațiunile de PUT si PATCH (atentie, modificările NU vor fi salvate, 
analizăm doar răspunsul). Ce observi ca este diferit între cele 2 metode?
'''
# put sterge ceea ce a fost inainte de payload
# patch pastraza ce e in payload si ce era dupa


