import requests

response = requests.get('http://localhost:8080/login')
print(f'Code: {response}, Data: {response.text}')

response = requests.get('http://localhost:8080/get?name=Gavin')
print(f'Code: {response}, Data: {response.text}')