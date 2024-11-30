import requests

url = "https://servicodados.ibge.gov.br/api/docs/"

resposta = requests.get(url)

print(resposta)
# print(resposta.text)

