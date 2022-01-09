from Banco import BancoO, BancoD

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
        comando = "insert into livrosO(nome, autor, genero, status, opiniao, dataa) values('"+ self.nome +"', '"+ self.autor + "','"+ self.genero +"','"+ self.status +"','"+ self.opiniao +"','"+ self.dataa +"')"
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
        for elemento in c:
            self.idlivro = elemento[0]
            self.nome = elemento[1]
            self.autor = elemento[2]
            self.genero = elemento[3]
            self.status = elemento[4]
            self.opiniao = elemento[5]
            self.dataa = elemento[6]
        c.close()
    
    def updateLivroO(self):
        banco = BancoO()
        c = banco.conexao.cursor()
        comando = "update livrosO set nome = '" + self.nome +"', autor = '" + self.autor +"', genero = '"+self.genero+"', status = '" +self.status+"', opiniao = '" +self.opiniao+"', data = '"+self.dataa+"'where idlivro = "+self.idlivro+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()

class LivroD:

    def __init__(self, idlivro=0, nome="", autor="", genero="", site="", valor="", dataa=""):
        self.info = {}
        self.idlivro = idlivro
        self.nome = nome
        self.autor = autor
        self.genero = genero
        self.site = site
        self.valor = valor
        self.dataa = dataa
    
    def insertLivroD(self):
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "insert into livrosD(nome, autor, genero, site, valor, dataa) values('"+ self.nome +"', '"+ self.autor + "','"+ self.genero +"','"+ self.site +"','"+ self.valor +"','"+ self.dataa +"')"
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
        for elemento in c:
            self.idlivro = elemento[0]
            self.nome = elemento[1]
            self.autor = elemento[2]
            self.genero = elemento[3]
            self.site = elemento[4]
            self.valor = elemento[5]
            self.dataa = elemento[6]
        c.close()
    
    def updateLivroD(self):
        banco = BancoD()
        c = banco.conexao.cursor()
        comando = "update livrosD set nome = '" + self.nome +"', autor = '" + self.autor +"', genero = '"+self.genero+"', site = '" +self.site+"', valor = '" +self.valor+"', data = '"+self.dataa+"'where idlivro = "+self.idlivro+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()