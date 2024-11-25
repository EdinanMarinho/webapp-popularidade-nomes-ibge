import requests

url = 'https://httpbin.org/get'

resposta = requests.post(url)
print( resposta.status_code)

# print(resposta.text)