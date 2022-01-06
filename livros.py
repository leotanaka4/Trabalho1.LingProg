from BancoO import BancoO
from BancoD import BancoD

class LivroO:

    def __init__(self, idlivro=0, nome="", autor="", genero="", status="", opiniao="", dataa=""):
        self.info = {}
        self.idlivro = idlivro
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.status = status
        self.opiniao = opiniao
        self.dataa = dataa
    
    def insertLivroO(self):
        banco = BancoO()
        c = banco.conexao.cursor()
        comando = "insert into livrosO(nome, autor, genero, status, opiniao, data) values('"+ self.nome +"', '"+ self.autor + "','"+ self.genero +"','"+ self.status +"','"+ self.opiniao +"','"+ self.data +"')"
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
    
    def updateLivroO(self):
        banco = BancoO()
        c = banco.conexao.cursor()
        comando = "update livrosO set nome = '" + self.nome +"', autor = '" + self.autor +"', genero = '"+self.genero+"', status = '" +self.status+"', opiniao = '" +self.opiniao+"', data = '"+self.data+"'where idlivro = "+self.idlivro+""
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
    
    def insertLivroD(self):
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "insert into livrosD(nome, autor, genero, site, valor, data) values('"+ self.nome +"', '"+ self.autor + "','"+ self.genero +"','"+ self.site +"','"+ self.valor +"','"+ self.data +"')"
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def deleteLivroD(self):
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "delete from livrosD where idlivro = "+self.idlivro+ " "
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def selectLivroD(self, id):
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "select * from livrosD where idlivro = " + str(id) + " "
        c.execute(comando)
        c.close()
    
    def updateLivroD(self):
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "update livrosD set nome = '" + self.nome +"', autor = '" + self.autor +"', genero = '"+self.genero+"', site = '" +self.site+"', valor = '" +self.valor+"', data = '"+self.data+"'where idlivro = "+self.idlivro+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()