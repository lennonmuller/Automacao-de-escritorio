from datetime import datetime



def salvar_comando(comando):
    try:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linha = f"{agora} - {comando}\n"

        with open("comandos_salvos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(linha)
        return "Comando salvo com sucesso!"
    
    except Exception as e:
        return f"Erro ao salvar o comando: {str(e)}"

def contar_comandos():
    try:
        with open("comandos_salvos.txt", "r", encoding="utf-8") as arquivo:
            comandos = arquivo.readlines()
        return len(comandos)
    
    except FileNotFoundError:
        return 0  # Retorna 0 se o arquivo não existir
    except Exception as e:
        return f"Erro ao contar os comandos: {str(e)}"