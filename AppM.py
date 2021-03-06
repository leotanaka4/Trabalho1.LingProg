from tkinter import *
from AppO import Obtidos
from AppD import Desejados

class Principal(Obtidos, Desejados):
    def __init__(self, master=None):

        self.fonte = ("Helvetica", "14")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 50
        self.container2["pady"] = 25
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 50
        self.container3["pady"] = 25
        self.container3.pack()
        
        self.titulo = Label(self.container1, text="Bookaholic")
        self.titulo["font"] = ("Times", "20", "bold")
        self.titulo.pack()

        self.btnObtidos = Button(self.container2, text="Obtidos",
        font=self.fonte, width=10, bg = '#7CB1F5', fg = 'white')
        self.btnObtidos["command"] = self.iniciarObtidos
        self.btnObtidos.pack(side=LEFT)

        self.btnDesejados = Button(self.container3, text="Desejados",
        font=self.fonte, width=10, bg = '#7CB1F5', fg = 'white')
        self.btnDesejados["command"] = self.iniciarDesejados
        self.btnDesejados.pack(side=LEFT)

    def iniciarObtidos(self):
        root1 = Tk()
        Obtidos(root1)
        root1.mainloop()
        
    def iniciarDesejados(self):
        root2 = Tk()
        Desejados(root2)
        root2.mainloop()

root = Tk()
Principal(root)
root.mainloop()