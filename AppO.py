from livros import LivrosO
from livros import LivrosD
from tkinter import *

#from <arquivo> import <classe ou método>

class Obtidos:

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
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["pady"] = 15
        self.container10.pack()


        self.titulo = Label(self.container1, text="Informe os dados do livro obtido:")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.status = ["Em Espera","Em curso","Finalizado"]

        self.lblidlivro = Label(self.container2,
        text="idlivro:", font=self.fonte, width=10)
        self.lblidlivro.pack(side=LEFT)

        self.txtidlivro = Entry(self.container2)
        self.txtidlivro["width"] = 10
        self.txtidlivro["font"] = self.fonte
        self.txtidlivro.pack(side=LEFT)

        self.btnBuscar = Button(self.container3, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarlivro
        self.btnBuscar.pack(side=RIGHT)


        #Nome
        self.lblnome = Label(self.container4, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container4)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        '''self.lbltelefone = Label(self.container4, text="Telefone:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT) '''

        '''self.lblemail= Label(self.container5, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)'''

        #Autor
        self.lblautor= Label(self.container5, text="Autor:",
        font=self.fonte, width=10)
        self.lblautor.pack(side=LEFT)

        self.txtautor = Entry(self.container5)
        self.txtautor["width"] = 25
        self.txtautor["font"] = self.fonte
        self.txtautor.pack(side=LEFT)

        #Genero
        self.lblgenero= Label(self.container6, text="Genero:",
        font=self.fonte, width=10)
        self.lblgenero.pack(side=LEFT)

        self.txtgenero = Entry(self.container6)
        self.txtgenero["width"] = 25
        self.txtgenero["font"] = self.fonte
        self.txtgenero.pack(side=LEFT)

        #Opnião
        self.lblopiniao = Label(self.container7, text="Opinião:",
        font=self.fonte, width=10)
        self.lblopiniao.pack(side=LEFT)

        self.txtopiniao = Entry(self.container7)
        self.txtopiniao["width"] = 25
        self.txtopiniao["font"] = self.fonte
        self.txtopiniao.pack(side=LEFT)

        #dataa
        self.lbldataa = Label(self.container8, text="Data de Atualização:",
        font=self.fonte, width=10)
        self.lbldataa.pack(side=LEFT)

        self.txtdataa = Entry(self.container8)
        self.txtdataa["width"] = 25
        self.txtdataa["font"] = self.fonte
        self.txtdataa.pack(side=LEFT)


        '''self.lblsenha= Label(self.container7, text="Senha:",
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)'''

        tipo = StringVar()
        tipo.set(self.status[2])
        self.dropdown = OptionMenu(self.container10,tipo,*self.status,command=self.display_selected)
        self.dropdown.pack()



        self.bntInsert = Button(self.container8, text="Inserir",font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserir
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterar
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluir
        self.bntExcluir.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Criar tela",font=self.fonte, width=12)
        self.bntExcluir["command"] = self.criaTela
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserir(self):
        
        user = LivrosO()
        user.nome = self.txtnome.get()
        user.autor = self.txtautor.get()
        user.genero = self.txtgenero.get()
        user.opiniao = self.txtopiniao.get()
        user.dataa = self.txtdataa.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = user.insertUser()
        
    def display_selected(self, escolha):
        pass 

    def alterar(self):
        
        user = LivrosO()
        #id está vazio
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.autor = self.txtautor.get()
        user.genero = self.txtgenero.get()
        user.opiniao = self.txtopiniao.get()
        user.dataa = self.txtdataa.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = user.updateUser()


    def excluir(self):
        user = LivrosO()
        user.idusuario = self.txtidusuario.get()

        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["Text"] = user.deleteUser()

    def buscar(self):
        user = LivrosO()
        id = self.txtidlivro.get()
        
        # aqui eu chamo a classe usuario para poder modificar coisas no banco de dados
        self.lblmsg["text"] = user.selectUser(id)

        self.txtidlivro.delete(0, END)
        self.txtidlivro.insert(INSERT, user.idlivro)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtautor.delete(0, END)
        self.txtautor.insert(INSERT,user.autor)

        self.txtgenero.delete(0, END)
        self.txtgenero.insert(INSERT, user.genero)

        self.txtopiniao.delete(0, END)
        self.txtopiniao.insert(INSERT, user.opiniao)

        self.txtdataa.delete(0, END)
        self.txtdataa.insert(INSERT,user.dataa)

    def criaTela(self):
        root2 = Tk()
        root2.title("Nova Janela")
        cont1 = Frame(root2)
        cont1.pack()
        titulo = Label(root2, text="Nova Tela")
        titulo["font"] = ("Calibri", "9", "bold")
        titulo.pack ()
        root2.mainloop()

        
        

root = Tk()
Obtidos(root)
root.mainloop()
