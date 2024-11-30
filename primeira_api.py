import requests
from pprint import pprint

nome = 'jessica'

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

resposta = requests.post(url)

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print( f'Erro no request:: {e}' )
    resultado = None
else:
    resultado = resposta.json()
    pprint(resultado[0]['res'])