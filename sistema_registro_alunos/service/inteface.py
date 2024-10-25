import tkinter as tk
from tkinter import ttk, messagebox
from main import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Sistema de Registro de Alunos")

        create_table()

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill="x", pady=10)

        title_label = tk.Label(self.top_frame, text="Sistema de Registro de Alunos", font=("Helvetica", 16, "bold"))
        title_label.pack(side=tk.LEFT, padx=20)

        self.middle_frame = tk.Frame(self)
        self.middle_frame.pack(side=tk.TOP, fill="both", expand=True, padx=20)


        labels = ["Nome", "Email", "Telefone", "Sexo", "Data de nascimento", "Endereço", "Curso"]
        self.entries = {}
        for idx, label in enumerate(labels):
            tk.Label(self.middle_frame, text=label).grid(row=idx, column=0, padx=10, pady=5)
            entry = tk.Entry(self.middle_frame, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[label] = entry
        
        self.entries['Sexo'] = ttk.Combobox(self.middle_frame, values=["Feminino", "Masculino"])
        self.entries['Sexo'].grid(row=3, column=1, padx=10, pady=5)
        
        self.entries['Curso'] = ttk.Combobox(self.middle_frame, values=["Engenharia", "Medicina", "Direito"])
        self.entries['Curso'].grid(row=6, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack(side=tk.TOP, pady=10)

        add_btn = tk.Button(btn_frame, text="Adicionar", command=self.add_student)
        add_btn.pack(side=tk.LEFT, padx=10)

        update_btn = tk.Button(btn_frame, text="Atualizar", command=self.update_student)
        update_btn.pack(side=tk.LEFT, padx=10)

        delete_btn = tk.Button(btn_frame, text="Deletar", command=self.delete_student)
        delete_btn.pack(side=tk.LEFT, padx=10)

        # Treeview (Tabela de alunos)
        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Email", "Telefone", "Sexo", "Data", "Endereço", "Curso"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="E-mail")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.heading("Data", text="Data de Nascimento")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.heading("Curso", text="Curso")
        
        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=100)
        self.tree.column("Email", width=100)
        self.tree.column("Telefone", width=100)
        self.tree.column("Sexo", width=50)
        self.tree.column("Data", width=100)
        self.tree.column("Endereço", width=150)
        self.tree.column("Curso", width=100)

        self.tree.pack(side=tk.BOTTOM, fill="both", expand=True, padx=20, pady=10)
        
        self.load_students()

    def add_student(self):
        nome = self.entries["Nome"].get()
        email = self.entries["Email"].get()
        contato = self.entries["Telefone"].get()
        sexo = self.entries["Sexo"].get()
        data_nascimento = self.entries["Data de nascimento"].get()
        endereco = self.entries["Endereço"].get()
        curso = self.entries["Curso"].get()

        insert_student(nome, email, contato, sexo, data_nascimento, endereco, curso)
        

        self.load_students()

    def update_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Erro", "Selecione um aluno para atualizar.")
            return
        
        student_id = self.tree.item(selected_item, 'values')[0]
        nome = self.entries["Nome"].get()
        email = self.entries["Email"].get()
        contato = self.entries["Telefone"].get()
        sexo = self.entries["Sexo"].get()
        data_nascimento = self.entries["Data de nascimento"].get()
        endereco = self.entries["Endereço"].get()
        curso = self.entries["Curso"].get()

        update_student(student_id, nome, email, contato, sexo, data_nascimento, endereco, curso)
        

        self.load_students()

    def delete_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Erro", "Selecione um aluno para deletar.")
            return

        student_id = self.tree.item(selected_item, 'values')[0]


        delete_student(student_id)

        self.load_students()


    def load_students(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        students = get_all_students()
        for student in students:
            self.tree.insert("", "end", values=student)


if __name__ == "__main__":
    app = App()
    app.mainloop()
