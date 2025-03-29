from flask import Flask, render_template, jsonify
from app import app
from app.controllers import obter_dados_simulados  # Importa a função de simulação

@app.route("/")  # ✅ Define a rota principal
def index():
    return render_template("index.html")  # Certifique-se de que o arquivo index.html existe!

@app.route("/dados")  # ✅ Cria uma rota para fornecer os dados simulados em JSON
def dados():
    return jsonify(obter_dados_simulados())  # Retorna os dados simulados em formato JSON
