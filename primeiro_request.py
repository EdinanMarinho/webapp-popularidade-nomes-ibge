import requests

url = "https://google.com?param1=valor1"

resposta = requests.get(url)

print(resposta)
print(resposta.text)

