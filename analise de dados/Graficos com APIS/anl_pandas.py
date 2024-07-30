import pandas as pd
import matplotlib.pyplot as plt

#Series
#pode conter qualquer tipo de dado(string, int, float, etc ). Semelhante a um array ou uma tabela do Banco de Dados
#CODIGO INICIO
# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)
#CODIGO FIM






#Dataframe
#Semelhante a uma tabela de registros no banco de dados, onde cada coluna tem uma informação
#CODIGO INICIO
# data = {
#     'Nome': ['Ana', 'João', 'Maria', 'Pedro'],
#     'Idade': [28, 22, 35, 32],
#     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador']
# }

# df = pd.DataFrame(data)
# print(df)
#CODIGO FIM





#Leitura e Escrita de Dados
#Pandas permite ler e escrever varios tipo de dados (CSV, JSON, Excel, SQL)
#CODIGO INICIO
# Leitura de um arquivo CSV
# df = pd.read_csv('escola_bd.sql')
# Escrita de um DataFrame para um arquivo CSV
# df.to_csv('teste.sql', index=False)
#CODIGO FIM





#Indexação e Seleção de Dados
#Pandas permite selecionar dados em Dataframe usando rótulos, posições, condições booleanas, etc
#CODIGO INICIO
# # Seleção de uma coluna
# print(df['Nome'])

# # Seleção de múltiplas colunas
# print(df[['Nome', 'Idade']])

# # Seleção de linhas por índice
# print(df.loc[0])  # Por rótulo
# print(df.iloc[0])  # Por posição

# # Seleção de linhas por condição
# print(df[df['Idade'] > 30])
#CODIGO FIM




#Manipulação de dados
#Pandas oferece várias funcionalidades para manipulação e transformação de dados.
#CODIGO INICIO
# # Adicionar uma coluna
# df['NovaColuna'] = df['Idade'] + 10
# print(df)
# print('\n')
# # Remover uma coluna
# df = df.drop('NovaColuna', axis=1)
# print(df)
# print('\n')
# # Renomear uma coluna
# df = df.rename(columns={'Nome': 'NomeCompleto'})
# print(df)
#CODIGO FIM



# Criação de um DataFrame
data = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro'],
    'Idade': [28, 22, 35, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador']
}
df = pd.DataFrame(data)

# Seleção de dados
print(df[['Nome', 'Idade']])
print(df[df['Idade'] > 30])

# Manipulação de dados
df['NovaColuna'] = df['Idade'] + 10
df = df.drop('NovaColuna', axis=1)

# Tratamento de dados faltantes (apenas um exemplo; não há dados faltantes neste caso)
df = df.fillna(0)

# Visualização e salvamento como imagem
plt.figure()
df['Idade'].plot(kind='hist')
plt.savefig('histograma_idades.png')  # Salva como imagem PNG
plt.close()  # Fecha a figura para liberar recursos

print("Imagem salva como 'histograma_idades.png'.")