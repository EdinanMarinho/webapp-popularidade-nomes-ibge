import os

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import dotenv

dotenv.load_dotenv()
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

auth = HTTPBasicAuth( username=client_id, password=client_secret )


url = "https://accounts.spotify.com/api/token"
body = {
    "grant_type": "client_credentials"
}

resposta = requests.post( url=url, data=body, auth=auth )

try:
    resposta.raise_for_status()
except requests.HTTPError as e:
    print(f'Erro no request{e}')
    resultado = None
else:
    resultado = resposta.json()

pprint(resultado)