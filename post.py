import requests


response = requests.post('http://localhost:8080/login', data={'name':'Gavin'})
print(f'Code: {response}, Data: {response.text}')