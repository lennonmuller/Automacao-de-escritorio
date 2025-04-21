from flask import Blueprint, render_template, request, jsonify
from app.controllers import salvar_comando, contar_comandos

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template("index.html")

@routes.route("/teste")
def teste():
    return "Testando rota personalizada!"

@routes.route("/salvar_comando", methods=["GET", "POST"])
def salvar():
    if request.method == "POST":
        comando = request.form.get("comando") or (request.guet_json() or {}).get("comando")

        if not comando:
            return jsonify({"erro": "Comando inválido"}), 400
        
        resultado = salvar_comando(comando)

        #se veio de formulario retorna para a mesma pagina
        if request.form:
            return render_template("comandos.html", mensagem=resultado)
        
        # se veio do teste via API
        return jsonify({"mensagem": resultado})
    
    quantidade = contar_comandos()
    return render_template("comandos.html", quantidade=quantidade)

@routes.route("/historico", methods=["GET"])
def historico():
    filtro = request.args.get("filtro", "").lower()  # Pega o valor do filtro

    comandos = []
    try:
        with open("comandos_salvos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                if "-" in linha:
                    data, comando = linha.split(" - ", 1)
                    if filtro in comando.lower():
                        comandos.append((data.strip(), comando.strip()))
    except FileNotFoundError:
        comandos = []

    return render_template("historico.html", comandos=comandos)




