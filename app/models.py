# Arquivo para definir o banco de dados
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comando(db.Model):
    """
    Modelo para armazenar comandos de automação.
    """
    id = db.Column(db.Integer, primary_key=True)  # Chave primária
    comando = db.Column(db.String(50), nullable=False)  # Comando a ser executado
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())  # Data e hora do comando

    def __repr__(self):
        return f"<Comando {self.comando}>"  # Representação do objeto para facilitar o debug