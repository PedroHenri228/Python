import tkinter as tk
from tkinter import ttk  # Para usar o Treeview
from process import obter_dados_json

# Função para exibir os dados na tabela (Treeview)
def exibir_dados_tabela():
    dados = obter_dados_json()  # Obtém os dados do JSON
    
    for dado in dados:
        tree.insert("", "end", values=(dado["ID"], dado["Nome"], dado["Valor"], dado["Quantidade"]))

# Criando a janela principal
janela = tk.Tk()
janela.title("Tabela de Dados JSON")

# Criando o Treeview (tabela)
colunas = ("ID", "Nome", "Valor", "Quantidade")
tree = ttk.Treeview(janela, columns=colunas, show="headings")

# Definindo os cabeçalhos da tabela
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Valor", text="Valor")
tree.heading("Quantidade", text="Quantidade")

# Definindo a largura das colunas
tree.column("ID", width=50)
tree.column("Nome", width=150)
tree.column("Valor", width=100)
tree.column("Quantidade", width=100)

# Empacotando a tabela na interface
tree.pack(pady=20)

# Chama a função para exibir os dados na tabela
exibir_dados_tabela()

# Loop da interface gráfica
janela.mainloop()
