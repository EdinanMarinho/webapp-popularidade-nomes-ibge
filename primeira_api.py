import requests

nome = "joao"

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

resposta = requests.get(url)

print( resposta )