import requests

url = 'https://httpbin.org/get'
resposta = requests.get(url)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Impossível fazer request! Erro: {e}')
else:
    print('Resultado:')
    print(resposta.json())