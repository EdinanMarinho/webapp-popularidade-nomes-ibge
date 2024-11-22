import requests

url = "https://edinanmarinho.com.br"

resposta = requests.get(url)

print(resposta)
print(resposta.text)

# with open('pagina_google.html', 'w') as arquivo:
#     arquivo.write(resposta.text)
