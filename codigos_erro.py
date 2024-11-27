import requests

url = 'https://httpbin.org/get'

resposta = requests.post(url)
resposta.raise_for_status()

# print(resposta.text)