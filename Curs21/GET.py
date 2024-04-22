import requests
from pprint import pprint

# variabila care ne tine adresa
URL = 'https://jsonplaceholder.typicode.com/'
response = requests.get(f'{URL}/posts/1')

# verificam statusul
if response.status_code == 200 :
    data = response.json()  # transformam continutul raspunsului din string in json
    pprint(data)
else:
    print('Request failed with status code: ', response.status_code)


