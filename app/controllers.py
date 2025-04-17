def salvar_comando(comando):
    try:
        with open("comandos_salvos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(comando + "\n")   # Adiciona uma nova linha após cada comando
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