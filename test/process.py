# processamento.py
import json

def obter_dados_json():
    """Simula o retorno de uma lista de JSON"""
    dados_json = '''
    [
        {"ID": 1, "Nome": "Produto A", "Valor": 100, "Quantidade": 50},
        {"ID": 2, "Nome": "Produto B", "Valor": 150, "Quantidade": 30},
        {"ID": 3, "Nome": "Produto C", "Valor": 200, "Quantidade": 20}
    ]
    '''
    return json.loads(dados_json)  # Converte a string JSON para lista de dicionários
