import requests
from pprint import pprint


url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

params = {
    "view":"nivelado"
}

def fazer_request(url, params=None):
    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print( f'Erro no request:: {e}' )
        resultado = None
    else:
        resultado = resposta.json()
    return resultado