from denuncias import Denuncia
from tkinter import *

#from <arquivo> import <classe ou método>

class Aplicacao:

    def __init__(self, master=None):

        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 10
        self.container12.pack()

        self.titulo = Label(self.container1, text="Mosquitômetro:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidusuario = Label(self.container2,
        text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarDenuncia
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail= Label(self.container5, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lbltipo= Label(self.container6, text="Tipo:",
        font=self.fonte, width=10)
        self.lbltipo.pack(side=LEFT)

        self.txttipo = Entry(self.container6)
        self.txttipo["width"] = 25
        self.txttipo["font"] = self.fonte
        self.txttipo.pack(side=LEFT)

        self.lblcidade= Label(self.container7, text="Cidade:",
        font=self.fonte, width=10)
        self.lblcidade.pack(side=LEFT)

        self.txtcidade = Entry(self.container7)
        self.txtcidade["width"] = 25
        self.txtcidade["font"] = self.fonte
        self.txtcidade.pack(side=LEFT)

        self.lblbairro= Label(self.container8, text="Bairro:",
        font=self.fonte, width=10)
        self.lblbairro.pack(side=LEFT)

        self.txtbairro = Entry(self.container8)
        self.txtbairro["width"] = 25
        self.txtbairro["font"] = self.fonte
        self.txtbairro.pack(side=LEFT)

        self.lblcep= Label(self.container9, text="CEP:",
        font=self.fonte, width=10)
        self.lblcep.pack(side=LEFT)

        self.txtcep = Entry(self.container9)
        self.txtcep["width"] = 25
        self.txtcep["font"] = self.fonte
        self.txtcep.pack(side=LEFT)

        self.lblidade= Label(self.container10, text="Idade:",
        font=self.fonte, width=10)
        self.lblidade.pack(side=LEFT)

        self.txtidade = Entry(self.container10)
        self.txtidade["width"] = 25
        self.txtidade["font"] = self.fonte
        self.txtidade.pack(side=LEFT)

        self.lblsenha= Label(self.container11, text="Senha:",
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container11)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container12, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirDenuncia
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container12, text="Alterar",font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarDenuncia
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container12, text="Excluir",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirDenuncia
        self.bntExcluir.pack(side=LEFT)

    def inserirDenuncia(self):
        
        caso = Denuncia()
        caso.nome = self.txtnome.get()
        caso.telefone = self.txttelefone.get()
        caso.email = self.txtemail.get()
        caso.tipo = self.txttipo.get()
        caso.cidade = self.txtcidade.get()
        caso.bairro = self.txtbairro.get()
        caso.cep = self.txtcep.get()
        caso.idade = self.txtidade.get()
        caso.senha = self.txtsenha.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = caso.insertUser()
        
    def display_selected(self, escolha):
        pass 

    def alterarDenuncia(self):
        
        caso = Denuncia()
        #id está vazio
        caso.idusuario = self.txtidusuario.get()
        caso.nome = self.txtnome.get()
        caso.telefone = self.txttelefone.get()
        caso.email = self.txtemail.get()
        caso.tipo = self.txttipo.get()
        caso.cidade = self.txtcidade.get()
        caso.bairro = self.txtbairro.get()
        caso.cep = self.txtcep.get()
        caso.idade = self.txtidade.get()
        caso.senha = self.txtsenha.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = caso.updateUser()


    def excluirDenuncia(self):
        caso = Denuncia()
        caso.idusuario = self.txtidusuario.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["Text"] = caso.deleteUser()

    def buscarDenuncia(self):
        caso = Denuncia()
        id = self.txtidusuario.get()
        
        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = caso.selectUser(id)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, caso.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, caso.nome)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, caso.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, caso.email)

        self.txttipo.delete(0, END)
        self.txttipo.insert(INSERT, caso.tipo)

        self.txtcidade.delete(0, END)
        self.txtcidade.insert(INSERT, caso.cidade)

        self.txtbairro.delete(0, END)
        self.txtbairro.insert(INSERT, caso.bairro)

        self.txtcep.delete(0, END)
        self.txtcep.insert(INSERT, caso.cep)

        self.txtidade.delete(0, END)
        self.txtidade.insert(INSERT, caso.idade)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, caso.senha)

root = Tk()
Aplicacao(root)
root.mainloop()