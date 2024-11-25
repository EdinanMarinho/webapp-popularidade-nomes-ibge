import requests

url = 'https://httpbin.org/get'

resposta = requests.get(url)
print( resposta.status_code)

# print(resposta.text)