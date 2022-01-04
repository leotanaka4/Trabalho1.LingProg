from BancoO import BancoO
from BancoD import BancoD

# ao tipo de sistema que 
# cria um elemento -> insert
#remove um elemento -> delete
#update de um elemento -> update
# busca um elemento -> select
# dá-se o nome de CRUD

class LivroO:

    def __init__(self, idlivro=0, nome="", autor="", genero="", status="", opiniao="", data=""):
        self.info = {}
        self.idlivro = idlivro
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.status = status
        self.opiniao = opiniao
        self.data = data
    
    def insertLivroO(self):

        banco = BancoO()

        c = banco.conexao.cursor()
        comando = "insert into livrosO(nome, autor, genero, status, opiniao) values('"+ self.nome +"', '"+ self.autor + "','"+ self.genero +"','"+ self.status +"','"+ self.opiniao +"','"+ self.data +"')"
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def deleteLivroO(self):
        banco = BancoO()

        c = banco.conexao.cursor()
        comando = "delete from livrosO where idlivro = "+self.idlivro+ " "
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def selectLivroO(self, id):
        banco = BancoO()

        c = banco.conexao.cursor()
        comando = "select * from livrosO where idlivro = " + str(id) + " "
        c.execute(comando)
        c.close()
    
    def updateUser(self):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "update usuarios set nome = '" + self.nome +"', telefone = '" + self.telefone +"', email = '"+self.email+"', usuario = '" +self.usuario+"',senha = '"+self.senha+"'where idusuario = "+self.idusuario+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()

class LivroD:

    def __init__(self, idlivro=0, nome="", autor="", genero="", site="", valor="", data=""):
        self.info = {}
        self.idlivro = idlivro
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.site = site
        self.valor = valor
        self.data = data