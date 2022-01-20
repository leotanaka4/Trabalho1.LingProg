from livros import LivroD
from tkinter import *

#from <arquivo> import <classe ou método>

class Desejados:

    def __init__(self, master=None):

        self.fonte = ("Verdana", "10")
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
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["pady"] = 15
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["pady"] = 15
        self.container11.pack()


        self.titulo = Label(self.container1, text="Informe os dados dos livros desejados:")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack ()

        #ID Livro
        self.lblidlivro = Label(self.container2,
        text="ID Livro:", font=self.fonte, width=10)
        self.lblidlivro.pack(side=LEFT)

        self.txtidlivro = Entry(self.container2)
        self.txtidlivro["width"] = 10
        self.txtidlivro["font"] = self.fonte
        self.txtidlivro.pack(side=LEFT)

        #Buscar
        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10, bg = '#7CB1F5', fg = 'white')
        self.btnBuscar["command"] = self.buscar
        self.btnBuscar.pack(side=RIGHT)

        #Nome
        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        #Autor
        self.lblautor= Label(self.container4, text="Autor:",
        font=self.fonte, width=10)
        self.lblautor.pack(side=LEFT)

        self.txtautor = Entry(self.container4)
        self.txtautor["width"] = 25
        self.txtautor["font"] = self.fonte
        self.txtautor.pack(side=LEFT)

        #Genero
        self.lblgenero= Label(self.container5, text="Genero:",
        font=self.fonte, width=10)
        self.lblgenero.pack(side=LEFT)

        self.txtgenero = Entry(self.container5)
        self.txtgenero["width"] = 25
        self.txtgenero["font"] = self.fonte
        self.txtgenero.pack(side=LEFT)

        #Site
        self.lblsite = Label(self.container6, text="Site:",
        font=self.fonte, width=10)
        self.lblsite.pack(side=LEFT)

        self.txtsite = Entry(self.container6)
        self.txtsite["width"] = 25
        self.txtsite["font"] = self.fonte
        self.txtsite.pack(side=LEFT)

        #Valor
        self.lblvalor = Label(self.container7, text="Valor:",
        font=self.fonte, width=10)
        self.lblvalor.pack(side=LEFT)

        self.txtvalor = Entry(self.container7)
        self.txtvalor["width"] = 25
        self.txtvalor["font"] = self.fonte
        self.txtvalor.pack(side=LEFT)

        #DataA
        self.lbldataa = Label(self.container8, text="Data:",
        font=self.fonte, width=10)
        self.lbldataa.pack(side=LEFT)

        self.txtdataa = Entry(self.container8)
        self.txtdataa["width"] = 25
        self.txtdataa["font"] = self.fonte
        self.txtdataa.pack(side=LEFT)

        #Inserir
        self.bntInsert = Button(self.container9, text="Inserir",font=self.fonte, width=12, bg = '#7CB1F5', fg = 'white')
        self.bntInsert["command"] = self.inserir
        self.bntInsert.pack (side=LEFT)

        #Alterar
        self.bntAlterar = Button(self.container9, text="Alterar",font=self.fonte, width=12, bg = '#7CB1F5', fg = 'white')
        self.bntAlterar["command"] = self.alterar
        self.bntAlterar.pack (side=LEFT)

        #Excluir
        self.bntExcluir = Button(self.container9, text="Excluir",font=self.fonte, width=12, bg = '#7CB1F5', fg = 'white')
        self.bntExcluir["command"] = self.excluir
        self.bntExcluir.pack(side=LEFT)
        
        #Comprado
        self.bntComprar = Button(self.container10, text="Comprar",font=self.fonte, width=12, bg = '#7CB1F5', fg = 'white')
        self.bntComprar["command"] = self.comprar
        self.bntComprar.pack(side=LEFT)

        #Feedback
        self.lblmsg = Label(self.container11, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserir(self):
        
        user = LivroD()
        user.nome = self.txtnome.get()
        user.autor = self.txtautor.get()
        user.genero = self.txtgenero.get()
        user.site = self.txtsite.get()
        user.valor = self.txtvalor.get()
        user.dataa = self.txtdataa.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = user.insertLivroD()

    def alterar(self):
        
        user = LivroD()
        #id está vazio
        user.idlivro = self.txtidlivro.get()
        user.nome = self.txtnome.get()
        user.autor = self.txtautor.get()
        user.genero = self.txtgenero.get()
        user.site = self.txtsite.get()
        user.valor = self.txtvalor.get()
        user.dataa = self.txtdataa.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = user.updateLivroD()


    def excluir(self):
        user = LivroD()
        user.idlivro = self.txtidlivro.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["Text"] = user.deleteLivroD()

    def buscar(self):
        user = LivroD()
        id = self.txtidlivro.get()
        
        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = user.selectLivroD(id)

        self.txtidlivro.delete(0, END)
        self.txtidlivro.insert(INSERT, user.idlivro)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtautor.delete(0, END)
        self.txtautor.insert(INSERT,user.autor)

        self.txtgenero.delete(0, END)
        self.txtgenero.insert(INSERT, user.genero)

        self.txtsite.delete(0, END)
        self.txtsite.insert(INSERT, user.site)

        self.txtvalor.delete(0, END)
        self.txtvalor.insert(INSERT, user.valor)

        self.txtdataa.delete(0, END)
        self.txtdataa.insert(INSERT,user.dataa)
    
    def comprar(self):
        user = LivroD()
        id = self.txtidlivro.get()

        self.lblmsg["Text"] = user.transferLivroD(id)