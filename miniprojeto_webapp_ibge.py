import requests
from pprint import pprint

def fazer_request(url, params=None):
    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print( f'Erro no request: {e}' )
        resultado = None
    else:
        resultado = resposta.json()
    return resultado


def pegar_nome_por_decada(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    dados_decadas = fazer_request( url=url )
    print(dados_decadas)

def main(nome):
    pegar_nome_por_decada(nome)

if __name__ == '__main__':
    main('Rafaela')