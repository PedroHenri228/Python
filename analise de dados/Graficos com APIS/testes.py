import pandas as pd


dados = {
    'Carros': ['Fiat Uno', 'Honda Civic', 'Ford KAR'],
    'Ano': ['2012', '2021', '2019'],
    'Preco': ['R$ 15000', ' R$ 25000', 'R$ 18000']
}


df_dados =pd.DataFrame(dados)
df_dados.to_excel("dados.xlsx")
