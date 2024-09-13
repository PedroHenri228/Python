import os
from pathlib import Path
import pandas as pd
import time

past =  Path('./arquivos_salvos')

files = os.listdir(past)
excel =  os.listdir('./excel')
def main():
    while True:
        
        loop_controller = False
        
        for file in files:
            if file.endswith('.txt'):
                caminho_completo = os.path.join(past, file)
                print(f"Arquivos encontrados: {caminho_completo}")
                
        nome_arquivo = input("Selecione o arquivo: ")
        df = pd.read_csv(f"./{past}/{nome_arquivo}")

        try:
            if os.path.exists(f"./{past}/{nome_arquivo}"):
                
                print(f"Arquivo selecionado {nome_arquivo} no caminho {past}/{nome_arquivo}")
                
                arquivo_excel = input("Defina um nome para o arquivo excel ")
                
                for files_excel in excel:
                    if files_excel.endswith('.xlsx'):
                        nome_arquivo_excel = os.path.basename(files_excel)        
                        if nome_arquivo_excel == f"{arquivo_excel}.xlsx":
                            os.system("cls")
                            print("Arquivo ja existe na pasta 'excel'\nDefina um nome válido")
                            
                            time.sleep(5)
                            os.system("cls")
                        else:
                            df.to_excel(f"./excel/{arquivo_excel}.xlsx")
                            os.system("cls")
                            print("Arquivo salvo na pasta 'excel'")
                            time.sleep(5)
                            loop_controller = True
                    else:
                        print("Arquivos não encontrados")
                        break
            else:
                print("Erro em achar o arquivo!!!")
                break
        except df.empty:
            print("Variavel vazia!!!!!")
            break
    
        if loop_controller:
            print("Programa Encerrado")
            break
        
if __name__ == "__main__":
    main()
