import os
from datetime import datetime

# Mensagem com data e hora atual
mensagem = f"Commit automático - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

# Comandos git
os.system("git add .")
os.system(f'git commit -m "{mensagem}"')
os.system("git push")