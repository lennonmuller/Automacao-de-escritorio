import os

# Diretório base do projeto
base_dir = "automacao_escritorio"

# Estrutura de pastas
folders = [
    "app",
    "app/static",
    "app/templates",
    "tests",
]

# Criar todas as pastas primeiro
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Arquivos do projeto
files = {
    "app/__init__.py": "",
    "app/routes.py": "# Arquivo para definir as rotas",
    "app/models.py": "# Arquivo para definir o banco de dados",
    "app/controllers.py": "# Arquivo para lógica do sistema",
    "config.py": "# Configurações do projeto",
    "run.py": "# Ponto de entrada do sistema",
    "requirements.txt": "# Lista de dependências",
}

# Criar os arquivos
for file, content in files.items():
    file_path = os.path.join(base_dir, file)
    # Criar diretório do arquivo, se não existir
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Criar e escrever o arquivo
    with open(file_path, "w") as f:
        f.write(content)

print("Estrutura do projeto criada com sucesso! 🚀")
