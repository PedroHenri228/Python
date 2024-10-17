import tkinter as tk

def insert():
    nome_arquivo = nome_entrada.get().strip() 
    texto = texto_entrada.get("1.0", tk.END).strip() 



janela = tk.Tk()
janela.title("Interface")
janela.geometry("800x800")

label_nome = tk.Label(janela, text="Inserir:")
label_nome.pack(pady=5)
nome_entrada = tk.Entry(janela, width=55)
nome_entrada.pack(pady=5)

label_text = tk.Label(janela, text="Teste:")
label_text.pack(pady=5)
texto_entrada = tk.Text(janela, width=40, height=10)
texto_entrada.pack(pady=5)

janela.mainloop()



