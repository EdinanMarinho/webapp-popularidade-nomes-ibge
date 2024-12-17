import requests
import pandas    as pd
import streamlit as st 

from pprint import pprint

def fazer_request(url, params=None):
    resposta = requests.get(url=url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print( f'Erro no request:{e}' )
        resultado = None
    else:
        resultado = resposta.json()
    return resultado


def pegar_nome_por_decada(nome):
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
    dados_decadas = fazer_request( url=url )
    dict_decadas = {}
    for dados in dados_decadas[0]['res']:
        decada = dados['periodo']
        quantidade = dados['frequencia']
        dict_decadas[decada] =  quantidade
    return dict_decadas


def main():
    st.title('Web App Nomes')
    st.write('Dados do IBGE (fonte: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')
    nome  = st.text_input('Consulte um nome:')
    if not nome:
        st.stop()
    dict_decadas = pegar_nome_por_decada(nome)
    df = pd.DataFrame.from_dict(dict_decadas, orient='index')

    st.dataframe(df)

if __name__ == '__main__':
    main()