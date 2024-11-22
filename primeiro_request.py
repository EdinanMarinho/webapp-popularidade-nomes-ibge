import requests

url = "https://google.com"

resposta = requests.get(url)

print(resposta)
print(resposta.text)

# with open('pagina_google.html', 'w') as arquivo:
#     arquivo.write(resposta.text)
