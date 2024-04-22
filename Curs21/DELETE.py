import requests
from pprint import pprint

# variabila care ne tine adresa
URL = 'https://jsonplaceholder.typicode.com/'

response = requests.delete(f'{URL}/posts/1')

if response.status_code == 200:
    print('Deleted successfully')
else:
    print('Request failed with status code: ', response.status_code)