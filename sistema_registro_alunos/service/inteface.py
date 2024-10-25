import tkinter as tk
from tkinter import ttk
from main import *  

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.show_frame(HomePage)

    def show_frame(self, frame_class):
        frame = frame_class(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Email", "Contato", "Sexo", "Data Nascimento", "Endereço", "Curso"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email", text="E-mail")
        self.tree.heading("Contato", text="Contato")
        self.tree.heading("Sexo", text="Sexo")
        self.tree.heading("Data Nascimento", text="Data Nascimento")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.heading("Curso", text="Curso")

        self.tree.column("ID", width=50)
        self.tree.column("Nome", width=100)
        self.tree.column("Email", width=100)
        self.tree.column("Contato", width=100)
        self.tree.column("Sexo", width=100)
        self.tree.column("Data Nascimento", width=100)
        self.tree.column("Endereço", width=100)
        self.tree.column("Curso", width=100)
        
        self.tree.pack(fill="both", expand=True)
        
        btn = tk.Button(self, text="Cadastrar Novo Aluno", 
                        command=lambda: controller.show_frame(SecondPage))
        btn.pack(pady=10)
        
        btn = tk.Button(self, text="Deletar Aluno", 
                        command=lambda: controller.show_frame(ThirdPage))
        btn.pack(pady=10)
        
        btn = tk.Button(self, text="Editar Aluno", 
                        command=lambda: controller.show_frame(FourthPage))
        btn.pack(pady=10)

        self.get_students()

    def get_students(self):
        students = get_all_students() 
        
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for student in students:
            self.tree.insert("", tk.END, values=student)  

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Cadastro de Alunos")
        label.pack(pady=10)
        
        btn = tk.Button(self, text="Voltar para tela inicial", 
                        command=lambda: controller.show_frame(HomePage))
        btn.pack()
        
        label_nome = tk.Label(self, text="Nome:")
        label_nome.pack(pady=5)
        self.nome_student = tk.Entry(self, width=55)
        self.nome_student.pack(pady=5)
        
        label_email = tk.Label(self, text="E-mail:")
        label_email.pack(pady=5)
        self.email_student = tk.Entry(self, width=55)
        self.email_student.pack(pady=5)
        
        label_contato = tk.Label(self, text="Contato:")
        label_contato.pack(pady=5)
        self.contato_student = tk.Entry(self, width=55)
        self.contato_student.pack(pady=5)
        
        label_sexo = tk.Label(self, text="Sexo:")
        label_sexo.pack(pady=5)
        self.sexo_student = tk.Entry(self, width=55)
        self.sexo_student.pack(pady=5)
        
        label_nascimento = tk.Label(self, text="Data de Nascimento:")
        label_nascimento.pack(pady=5)
        self.nasc_student = tk.Entry(self, width=55)
        self.nasc_student.pack(pady=5)
        
        label_endereco = tk.Label(self, text="Endereço:")
        label_endereco.pack(pady=5)
        self.endereco_student = tk.Entry(self, width=55)
        self.endereco_student.pack(pady=5)
        
        label_curso = tk.Label(self, text="Curso:")
        label_curso.pack(pady=5)
        self.curso_student = tk.Entry(self, width=55)
        self.curso_student.pack(pady=5)

        btn_insert = tk.Button(self, text="Inserir Estudante", command=self.insert)
        btn_insert.pack(pady=10)

    def insert(self):
        nome = self.nome_student.get()
        email = self.email_student.get()
        contato = self.contato_student.get()
        sexo = self.sexo_student.get()
        nasc = self.nasc_student.get()
        endereco = self.endereco_student.get()
        curso = self.curso_student.get()
        
        insert_student(nome, email, contato, sexo, nasc, endereco, curso)  

        self.nome_student.delete(0, tk.END) 
        self.email_student.delete(0, tk.END) 
        self.contato_student.delete(0, tk.END) 
        self.sexo_student.delete(0, tk.END) 
        self.nasc_student.delete(0, tk.END) 
        self.endereco_student.delete(0, tk.END) 
        self.curso_student.delete(0, tk.END) 

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Excluir Aluno")
        label.pack(pady=10)
        btn = tk.Button(self, text="Voltar para tela inicial", 
                        command=lambda: controller.show_frame(HomePage))
        btn.pack()

        label_id = tk.Label(self, text="Identificação:")
        label_id.pack(pady=5)
        self.id_student = tk.Entry(self, width=55)
        self.id_student.pack(pady=5)
        
        btn_insert = tk.Button(self, text="Deletar Estudante", command=self.delete)
        btn_insert.pack(pady=10)
        
    def delete(self):
        student_id = self.id_student.get()
        delete_student(student_id)
        self.id_student.delete(0, tk.END) 

class FourthPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Editar Aluno")
        label.pack(pady=10)
        
        btn = tk.Button(self, text="Voltar para tela inicial", 
                        command=lambda: controller.show_frame(HomePage))
        btn.pack()
        
        label_id = tk.Label(self, text="ID do Aluno:")
        label_id.pack(pady=5)
        self.id_student = tk.Entry(self, width=55)
        self.id_student.pack(pady=5)
        
        label_nome = tk.Label(self, text="Novo Nome:")
        label_nome.pack(pady=5)
        self.nome_student = tk.Entry(self, width=55)
        self.nome_student.pack(pady=5)

        label_email = tk.Label(self, text="Novo E-mail:")
        label_email.pack(pady=5)
        self.email_student = tk.Entry(self, width=55)
        self.email_student.pack(pady=5)

        label_contato = tk.Label(self, text="Novo Contato:")
        label_contato.pack(pady=5)
        self.contato_student = tk.Entry(self, width=55)
        self.contato_student.pack(pady=5)

        label_sexo = tk.Label(self, text="Novo Sexo:")
        label_sexo.pack(pady=5)
        self.sexo_student = tk.Entry(self, width=55)
        self.sexo_student.pack(pady=5)

        label_nascimento = tk.Label(self, text="Nova Data de Nascimento:")
        label_nascimento.pack(pady=5)
        self.nasc_student = tk.Entry(self, width=55)
        self.nasc_student.pack(pady=5)

        label_endereco = tk.Label(self, text="Novo Endereço:")
        label_endereco.pack(pady=5)
        self.endereco_student = tk.Entry(self, width=55)
        self.endereco_student.pack(pady=5)

        label_curso = tk.Label(self, text="Novo Curso:")
        label_curso.pack(pady=5)
        self.curso_student = tk.Entry(self, width=55)
        self.curso_student.pack(pady=5)

        btn_update = tk.Button(self, text="Atualizar Aluno", command=self.update)
        btn_update.pack(pady=10)

    def update(self):
        student_id = self.id_student.get()
        nome = self.nome_student.get()
        email = self.email_student.get()
        contato = self.contato_student.get()
        sexo = self.sexo_student.get()
        nasc = self.nasc_student.get()
        endereco = self.endereco_student.get()
        curso = self.curso_student.get()

        update_student(student_id, nome, email, contato, sexo, nasc, endereco, curso)

        self.id_student.delete(0, tk.END)
        self.nome_student.delete(0, tk.END)
        self.email_student.delete(0, tk.END)
        self.contato_student.delete(0, tk.END)
        self.sexo_student.delete(0, tk.END)
        self.nasc_student.delete(0, tk.END)
        self.endereco_student.delete(0, tk.END)
        self.curso_student.delete(0, tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
