import requests

url = 'https://httpbin.org/get'
resposta = requests.get(url)

print( resposta.text )