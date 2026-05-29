from tkinter import *
from tkinter import messagebox

class SistemaCadastro:

    def __init__(self, master):

        self.master = master
        self.master.title("Sistema de Cadastro")
        self.master.geometry("600x500")
        self.master.configure(bg="#f0f0f0")

        # TÍTULO
        self.titulo = Label(
            master,
            text="Cadastro de Alunos",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        self.titulo.pack(pady=20)

        # FRAME FORMULÁRIO
        self.frame_form = Frame(master, bg="#ffffff", bd=2,
relief="solid")
        self.frame_form.pack(pady=10, padx=20, fill="x")

        # NOME
        self.lbl_nome = Label(
            self.frame_form,
            text="Nome:",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.lbl_nome.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nome = Entry(
            self.frame_form,
            font=("Arial", 12),
            width=30
        )
        self.entry_nome.grid(row=0, column=1, padx=10)

        # IDADE
        self.lbl_idade = Label(
            self.frame_form,
            text="Idade:",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.lbl_idade.grid(row=1, column=0, padx=10, pady=10)

        self.entry_idade = Entry(
            self.frame_form,
            font=("Arial", 12),
            width=30
        )
        self.entry_idade.grid(row=1, column=1)

        # CURSO
        self.lbl_curso = Label(
            self.frame_form,
            text="Curso:",
            font=("Arial", 12),
            bg="#ffffff"
        )
        self.lbl_curso.grid(row=2, column=0, padx=10, pady=10)

        self.entry_curso = Entry(
            self.frame_form,
            font=("Arial", 12),
            width=30
        )
        self.entry_curso.grid(row=2, column=1)

        # BOTÕES
        self.frame_botoes = Frame(master, bg="#f0f0f0")
        self.frame_botoes.pack(pady=15)

        self.btn_cadastrar = Button(
            self.frame_botoes,
            text="Cadastrar",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15,
            command=self.cadastrar
        )
        self.btn_cadastrar.grid(row=0, column=0, padx=10)

        self.btn_limpar = Button(
            self.frame_botoes,
            text="Limpar",
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            width=15,
            command=self.limpar
        )
        self.btn_limpar.grid(row=0, column=1, padx=10)

        # LISTA
        self.lista = Listbox(
            master,
            font=("Arial", 11),
            width=70,
            height=10
        )
        self.lista.pack(pady=20)

    # FUNÇÃO CADASTRAR
    def cadastrar(self):

        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        curso = self.entry_curso.get()

        if nome == "" or idade == "" or curso == "":
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos!"
            )
        else:
            texto = f"Nome: {nome} | Idade: {idade} | Curso: {curso}"

            self.lista.insert(END, texto)

            messagebox.showinfo(
                "Sucesso",
                "Aluno cadastrado!"
            )

            self.limpar()

    # FUNÇÃO LIMPAR
    def limpar(self):

        self.entry_nome.delete(0, END)
        self.entry_idade.delete(0, END)
        self.entry_curso.delete(0, END)

# JANELA PRINCIPAL
root = Tk()
SistemaCadastro(root)

root.mainloop()