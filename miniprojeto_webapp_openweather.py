import os

import requests
from pprint import pprint
import dotenv

import streamlit as st


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

def pegar_tempo_para_local(local):
    dotenv.load_dotenv()
    token = os.environ["CHAVE_API_OPENWEATHER"]

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': token,
        'q': local,
        'units': 'metric',
        'lang': 'pt_br',
    }
    dados_tempo = fazer_request( url=url, params=params )
    return dados_tempo

def main():
    st.title('Web App Tempo')
    st.write('Dados do OpenWeather (https://openweathermap.org/current)')
    local = st.text_input('Busque por um local:')
    if not local:
        st.stop()
    
    dados_tempo = pegar_tempo_para_local(local=local)
    if not dados_tempo:
        st.warning( f'Dados não encontrados para o local {local}')
        st.stop()

    print(dados_tempo)

if __name__ == '__main__':
    main()
