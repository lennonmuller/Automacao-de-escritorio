# Arquivo para definir as rotas
from app import app

@app.route('/')
def index():
    return "Bem-vindo ao Sistema de Automação de Escritório!"
