from sqlite3.dbapi2 import TimestampFromTicks
from Banco import Banco

# ao tipo de sistema que 
# cria um elemento -> insert
#remove um elemento -> delete
#update de um elemento -> update
# busca um elemento -> select
# dá-se o nome de CRUD

class Denuncia:

    def __init__(self, idusuario=0, nome="",telefone="",email="", tipo="", cidade="", bairro="", cep="", idade="",senha=""):
        self.info = {}
        self.idusuario=idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tipo = tipo
        self.cidade = cidade
        self.bairro = bairro
        self.cep = cep
        self.idade = idade
        self.senha = senha
    
    def insertUser(self):

        banco = Banco()

        c = banco.conexao.cursor()
        comando = "insert into usuarios(nome,telefone,email,tipo,cidade,bairro,cep,idade,senha) values('"+ self.nome +"', '"+ self.telefone + "','"+ self.email +"','"+ self.tipo +"','"+ self.cidade +"','"+ self.bairro +"','"+ self.cep +"','"+ self.idade +"','"+ self.senha +"')"
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def deleteUser(self):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "delete from usuarios where idusuario = "+self.idusuario+ " "
        c.execute(comando)
        banco.conexao.commit()
        c.close()

    def selectUser(self, id):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "select * from usuarios where idusuario = " + str(id) + " "
        c.execute(comando)

        # c recebe uma lista com os atributos

        print (c) #só para debug depois

        for elemento in c:
            self.idusuario = elemento[0]
            print(elemento[0])
            self.nome = elemento[1]
            print(elemento[1])
            self.telefone = elemento[2]
            print(elemento[2])
            self.email = elemento[3]
            print(elemento[3])
            self.tipo = elemento[4]
            print(elemento[4])
            self.cidade = elemento[5]
            print(elemento[5])
            self.bairro = elemento[6]
            print(elemento[6])
            self.cep = elemento[7]
            print(elemento[7])
            self.idade = elemento[8]
            print(elemento[8])
            self.senha = elemento[9]
            print(elemento[9])

        c.close()

    def updateUser(self):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "update usuarios set nome = '" + self.nome +"', telefone = '" + self.telefone +"', email = '"+self.email+"', tipo = '"+self.tipo+"', cidade = '"+self.cidade+"', bairro = '"+self.bairro+"', cep = '"+self.cep+"', idade = '"+self.idade+",senha = '"+self.senha+"'where idusuario = "+self.idusuario+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()