# Importa a biblioteca para conectar com a internet
import requests

# Define o endereço da API com o nome "lucas"
url = "https://api.agify.io?name=lucas"

# Faz a requisição e guarda a resposta
resposta = requests.get(url)


dados = resposta.json()
print(f"Nome: {dados['name']}")
print(f"Idade estimada: {dados['age']}")