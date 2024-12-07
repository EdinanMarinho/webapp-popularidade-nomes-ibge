import requests
from pprint import pprint


def pegar_ids_estados():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    params = {
        'view':'nivelado'
    }
    dados_estados = fazer_request(url=url, params=params)
    dict_estado = {}
    for dados in dados_estados:
        id_estado = dados['UF-id'] # extrair ids do estado
        nome_estado = dados['UF-nome'] # extrair nome estado
        dict_estado[id_estado] = nome_estado
    return dict_estado     


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


def main():
    dict_estados = pegar_ids_estados()
    pprint(dict_estados)

if __name__ == '__main__':
    main()