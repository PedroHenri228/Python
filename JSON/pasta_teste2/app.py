import json 

with open("dados.json", "r") as arquivo_json:
    dados_lidos = json.load(arquivo_json)


print(dados_lidos)