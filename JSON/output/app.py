import json #IMPORTANDO O JSON
import os #IMPORTANDO A BIBLIOTECA PARA CRIAÇÃO DAS PASTAS


dados = { #DICIONARIO COM OS DADOS QUE VÃO SER ENVIADOS PARA O JSON 
    "nome": "Pedro Henrique",
    "idade": 18,
    "Causa": "Testando JSON",
    "data": "29/06/2024"
}
pasta = 'output' #CRIANDO A PASTA "output"
arquivo = 'dados.json' #CRIADNDO O ARQUIVO "dados.json"
caminho_completo = os.path.join(pasta, arquivo) #CRIANDO O CAMINHO


os.makedirs(pasta, exist_ok=True) #GARANTIR QUE A PASTA EXISTE

with open(caminho_completo, 'w') as arquivo_json: #ESCREVENDO O ARQUIVO JSON
    json.dump(dados, arquivo_json, indent=4)
