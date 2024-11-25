import requests

url = 'https://httpbin.org/get'

resposta = requests.post(url)

print(resposta.json())