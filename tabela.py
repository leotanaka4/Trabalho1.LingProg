from tkinter import *
from Banco import *

class TableO:
    def __init__(self,root):
        self.lista = []
        banco = BancoO()
        c = banco.conexao.cursor()
        comando = "select * from livrosO;"
        c.execute(comando)
        for auxiliar in c:
            self.lista.append(auxiliar)

        self.total_rows = len(self.lista)
        self.total_columns = len(self.lista[0])
        c.close()

        for i in range(self.total_rows):
            for j in range(self.total_columns):
                        self.e = Entry(root, width=16, bg = '#7CB1F5', fg = 'white', font=('Arial',12,'bold')) 
                        self.e.grid(row=i, column=j) 
                        self.e.insert(END, self.lista[i][j])

class TableD:
    def __init__(self,root):
        self.lista = []
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "select * from livrosD;"
        c.execute(comando)
        for auxiliar in c:
            self.lista.append(auxiliar)

        self.total_rows = len(self.lista)
        self.total_columns = len(self.lista[0])
        c.close()

        for i in range(self.total_rows):
            for j in range(self.total_columns):
                        self.e = Entry(root, width=16, bg = '#7CB1F5', fg = 'white', font=('Arial',12,'bold')) 
                        self.e.grid(row=i, column=j) 
                        self.e.insert(END, self.lista[i][j])