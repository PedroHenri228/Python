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
        
        # Criação do Treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Email", "Contato", "Sexo" ,"Data Nascimento", "Endereço", "Curso"), show="headings")
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
        

        btn = tk.Button(self, text="Ir para tela 2", 
                        command=lambda: controller.show_frame(SecondPage))
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
        label = tk.Label(self, text="Segunda Tela")
        label.pack(pady=10)
        
        btn = tk.Button(self, text="Voltar para tela inicial", 
                        command=lambda: controller.show_frame(HomePage))
        btn.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
