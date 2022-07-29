import requests
from flask import Flask

print('Qual é o seu CEP?\n')
cep_client = input(str())

cep_client = cep_client.strip()

if len(cep_client) == 9:
    cep_client = cep_client.replace('-', "")


response = requests.get(f"https://viacep.com.br/ws/{cep_client}/json/")
response = response.json()

app = Flask(__name__)

# set FLASK_APP=main.py
# $env:FLASK_APP="client_api.py"
# flask run


@app.get('/')
def return_cep():
    return response
