import requests
from pprint import pprint

# variabila care ne tine adresa
URL = 'https://jsonplaceholder.typicode.com/'
payload = {
    'body': 'postare noua',
    'title': 'titlu nou',
    'userId': '2'
}  # id se pune automat

response = requests.post(f'{URL}/posts', json=payload)

if response.status_code == 201:
    data = response.json()  # transformam continutul raspunsului din string in json
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)
