# Importações necessárias
import random  # Para simular dados variáveis

def obter_dados_simulados():
    """
    Simula dados de sensores para automação de escritório.
    Retorna um dicionário com valores fictícios.
    """
    dados = {
        "temperatura": round(random.uniform(18, 28), 1),  # Temperatura entre 18°C e 28°C
        "umidade": round(random.uniform(30, 70), 1),  # Umidade entre 30% e 70%
        "luz_acesa": random.choice([True, False])  # Estado da luz (ligada/desligada)
    }
    return dados
