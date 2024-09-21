import tkinter as tk
from main import *  # Importando as funções de processamento

def mostrar():
    """Captura os dados dos campos e chama a função de processamento."""
    nome_arquivo = nome_entrada.get().strip()  # Captura o texto do campo de nome do arquivo
    texto = texto_entrada.get("1.0", tk.END).strip()  # Captura o texto do campo de texto
    
    txt_dir = "tx"  # Diretório onde o arquivo será salvo
    criar_texto(nome_arquivo, texto, txt_dir)  # Salva o arquivo
    listar_txt()  # Atualiza a lista de arquivos após salvar


def listar_txt():
    """Atualiza a lista de arquivos exibidos."""
    campo_saida.delete("1.0", tk.END)  # Limpa o campo antes de atualizar
    resultado = listar_arquivos()  # Obtém a lista de arquivos
    campo_saida.insert(tk.END, resultado)  # Exibe o resultado no campo de saída

def listar_excel():
    campo_saida_xlsx.delete("1.0", tk.END)  # Limpa o campo antes de atualizar
    resultado = listar_xlsx()  # Obtém a lista de arquivos
    campo_saida_xlsx.insert(tk.END, resultado)

def converter_excel():
    result = listar_arquivos()

    if result:  # Verifica se há arquivos na lista
        for file in result.split("\n"):
            salvar_xlsx(txt_dir / file)
    listar_excel()
    
# Criando a janela principal
janela = tk.Tk()
janela.title("Interface")
janela.geometry("800x800")

# Criando o campo de entrada para o nome do arquivo
label_nome = tk.Label(janela, text="Nome do Relatório:")
label_nome.pack(pady=5)
nome_entrada = tk.Entry(janela, width=55)
nome_entrada.pack(pady=5)

# Criando o campo de texto para o conteúdo
label_text = tk.Label(janela, text="Relatório:")
label_text.pack(pady=5)
texto_entrada = tk.Text(janela, width=40, height=10)
texto_entrada.pack(pady=5)

# Botão para salvar o arquivo
botao = tk.Button(janela, text="Salvar Arquivo em Texto", command=mostrar, bg="#015958", fg='white')
botao.pack(pady=10)  # Posiciona o botão antes da lista de arquivos

# Label para listar os arquivos
label_txt = tk.Label(janela, text="Lista de Arquivos Texto")
label_txt.pack(pady=10)


# Campo de saída para exibir a lista de arquivos
campo_saida = tk.Text(janela, width=40, height=5)
campo_saida.pack(pady=5)
botao = tk.Button(janela, text="Converter arquivo para excel", command=converter_excel, bg="#015958", fg='white')
botao.pack(pady=10)  # Posiciona o botão antes da lista de arquivos

label_txt = tk.Label(janela, text="Lista de Arquivos Excel")
label_txt.pack(pady=10)

campo_saida_xlsx = tk.Text(janela, width=40, height=5)
campo_saida_xlsx.pack(pady=5)

# Chama a função para exibir o resultado ao iniciar a interface
listar_txt()
listar_excel()
# Loop da interface gráfica
janela.mainloop()
