import os
from pathlib import Path
import re
import pandas as pd
import json

excel_dir = Path('./excel')  # diretório onde serão salvos os arquivos excel
txt_dir =  Path('./tx')
erro_message = ''  # Variável de erro vazia


def limpar_nome_arquivo(nome):
    """Remove caracteres inválidos do nome do arquivo."""
    return re.sub(r'[\/:*?"<>|\n\r]', '', nome)

def criar_texto(nome: str, texto: str, txt_dir: str):
    """Cria um arquivo com o nome e texto fornecidos."""
    nome = limpar_nome_arquivo(nome)
    
    # Cria o arquivo no diretório especificado
    with open(f"{txt_dir}/{nome}.txt", 'w') as arquivo_txt:
        arquivo_txt.write(texto)
    
    print(arquivo_txt)
    

def listar_arquivos():  # Função para listar todos arquivos
    files = os.listdir(txt_dir)  # Listando os arquivos txt
    
    txt_files = [file for file in files if file.endswith('.txt')]  # Estrutura para listar todos os arquivos txt

    if txt_files:
        return "\n".join(txt_files)  # Retorna os arquivos listados em uma string
    else:
        erro_message = "FileNotFoundError: não foi possível encontrar nenhum arquivo .txt"
        return erro_message


def salvar_xlsx(arquivo: Path):
    # Verifica se o arquivo é .txt
        try:
            # Lê o arquivo .txt
            df = pd.read_csv(arquivo, delimiter='\t', header=None, encoding='ISO-8859-1')
            
            if df.empty:
                print(f"Arquivo {arquivo.name} está vazio.")
            else:
                # Converte o arquivo .txt para .xlsx
                arquivo_excel = arquivo.with_suffix('.xlsx')  # Converte a extensão para .xlsx
                df.to_excel(excel_dir / arquivo_excel.name, index=False)  # Salva no diretório excel
                return arquivo_excel
        except FileNotFoundError:
            print(f"Erro: O arquivo {arquivo} não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo {arquivo}: {e}")

def listar_xlsx():
    files = os.listdir(excel_dir)
    
    xlsx_files = [file for file in files if file.endswith('.xlsx')]
    
    if xlsx_files:
        return "\n".join(xlsx_files)
    else:
        erro_message = "FileNotFoundError: não foi possível encontrar nenhum arquivo .xlsx"
        return erro_message
    
    