import pandas as pd
import flet as ft

data = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro Henrique'],
    'Idade': [28, 22, 35, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Juiz de Fora']
}

df = pd.DataFrame(data)


def criar_celula(conteudo):
    return ft.DataCell(ft.Text(str(conteudo), color="black"))

def main(page: ft.Page):
    
    page.bgcolor = ft.colors.WHITE

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome", color="black")),
            ft.DataColumn(ft.Text("Cidade", color="black")),
            ft.DataColumn(ft.Text("Idade", color="black"), numeric=True),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    criar_celula(df["Nome"][0]),
                    criar_celula(df["Cidade"][0]),
                    criar_celula(df["Idade"][0]),
                ],
            ),
            ft.DataRow(
                cells=[
                    criar_celula(df["Nome"][1]),
                    criar_celula(df["Cidade"][1]),
                    criar_celula(df["Idade"][1]),
                ],
            ),
            ft.DataRow(
                cells=[
                    criar_celula(df["Nome"][2]),
                    criar_celula(df["Cidade"][2]),
                    criar_celula(df["Idade"][2]),
                ],
            ),
            ft.DataRow(
                cells=[
                    criar_celula(df["Nome"][3]),
                    criar_celula(df["Cidade"][3]),
                    criar_celula(df["Idade"][3]),
                ],
            ),
        ],
    )

    page.add(
        ft.Container(
            content=tabela,
            alignment=ft.alignment.center,  
            padding=20 
        )
    )

ft.app(main)
