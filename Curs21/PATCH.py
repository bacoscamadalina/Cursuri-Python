import requests
from pprint import pprint

# variabila care ne tine adresa
URL = 'https://jsonplaceholder.typicode.com/'
payload = {
    'title': 'titlu nou 2'
}

response = requests.patch(f'{URL}/posts/1', json=payload)

if response.status_code == 200:
    data = response.json()  # transformam continutul raspunsului din string in json
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)

# PATCH pastreaza toata structura si modifica titlu 2