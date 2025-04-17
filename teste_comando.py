import requests

url = "http://127.0.0.1:5000/salvar_comando"
dados = {"comando": "Ligar luz do escritório"}

resposta = requests.post(url, json=dados)
print("Status:", resposta.status_code)
print("Resposta:", resposta.json())
