from tkinter import *
from AppO import Obtidos
from AppD import Desejados

class Principal(Obtidos, Desejados):
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
        
        self.titulo = Label(self.container1, text="Bookaholic")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.btnBuscar = Button(self.container2, text="Lista de Livros Obtidos",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.iniciarObtidos
        self.btnBuscar.pack(side=LEFT)

        self.btnBuscar = Button(self.container3, text="Lista de Livros Desejados",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.iniciarDesejados
        self.btnBuscar.pack(side=LEFT)

    def iniciarObtidos(self,):
        root1 = Tk()
        Obtidos(root1)
        root1.mainloop()
        
    def iniciarDesejados(self,):
        root2 = Tk()
        Desejados(root2)
        root2.mainloop()

