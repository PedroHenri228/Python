import requests
import flet as ft
import pandas as pd
import locale

response = requests.get('http://localhost:8080/datas')

def criar_celula(conteudo):
    return ft.DataCell(ft.Text(str(conteudo), color="black"))

def formatar_valor(valorBRL):
    valor = valorBRL
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor, grouping=True, symbol=None)

    return valor
    
def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE

    if response.status_code == 200:
        data = response.json()

        if data:
            nomes = [item.get('Nome') for item in data if 'Nome' in item]
            valores = [item.get('Valor') for item in data if 'Valor' in item]
            times = [item.get('Time') for item in data if 'Time' in item]

            pdn = {
                'Nome': nomes,
                'Valor': valores,
                'Data': times,
            }

            df = pd.DataFrame(pdn)

            colunas = [
                ft.DataColumn(ft.Text("Nome", color="black")),
                ft.DataColumn(ft.Text("Valor", color="black")),
                ft.DataColumn(ft.Text("Data", color="black")),
            ]

            linhas = []

            for _, row in df.iterrows():
                linhas.append(ft.DataRow([
                    criar_celula(row['Nome']),
                    criar_celula(formatar_valor(row['Valor'])),
                    criar_celula(row['Data']),
                ]))

            tabela = ft.DataTable(
                columns=colunas,
                rows=linhas,
            )

            page.add(
                ft.Container(
                    content=tabela,
                    alignment=ft.alignment.center,
                    padding=20
                )
            )
        else:
            print("A lista de dados está vazia.")
    else:
        print(f"Erro na requisição: {response.status_code}")

ft.app(main)
