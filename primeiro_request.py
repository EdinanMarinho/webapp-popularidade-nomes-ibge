import requests

url = "https://google.com"

resposta = requests.get(url)

print(resposta)
print(resposta.text)

