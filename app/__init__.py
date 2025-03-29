from flask import Flask

app = Flask(__name__)  # Criamos o app aqui

from app import routes  # ✅ Importamos routes depois de criar o app
