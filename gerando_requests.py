import requests

url = 'https://httpbin.org/post'

data = {
    "meus_dados": [1, 2, 3],
    "pessoa": {
        "nome": "Edinan",
        "Business Analyst Professional - Data Science": True
    }
}

resposta = requests.post(url, json=data)

print( resposta.json() )