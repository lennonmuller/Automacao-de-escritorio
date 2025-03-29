def rodar_simulacao(dado):
    # A lógica da sua simulação vai aqui
    # Por exemplo, vamos apenas simular que o dado é multiplicado por 2
    try:
        dado = float(dado)  # Tentando converter o dado para número
        resultado = dado * 2
        return f'O resultado da simulação é: {resultado}'
    except ValueError:
        return 'Erro: O dado inserido não é válido. Por favor, insira um número.'
