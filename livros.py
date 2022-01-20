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
        comando = "update livrosO set nome = '" + self.nome +"', autor = '" + self.autor +"', genero = '"+self.genero+"', status = '" +self.status+"', opiniao = '" +self.opiniao+"', dataa = '"+self.dataa+"'where idlivro = "+self.idlivro+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def countLivroO(self):
        banco = BancoO()
        lista = []
        c = banco.conexao.cursor()
        comando = "SELECT COUNT(status) FROM livroO WHERE status=" "Em espera" ""
        c.execute(comando)
        lista.append(c)
        comando = "SELECT COUNT(status) FROM livroO WHERE status=" "Em curso" ""
        c.execute(comando)
        lista.append(c)
        comando = "SELECT COUNT(status) FROM livroO WHERE status=" "Finalizado" ""
        c.execute(comando)
        lista.append(c)
        c.close()
        return lista

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
        comando = "update livrosD set nome = '" + self.nome +"', autor = '" + self.autor +"', genero = '"+self.genero+"', site = '" +self.site+"', valor = '" +self.valor+"', dataa = '"+self.dataa+"'where idlivro = "+self.idlivro+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()

    def transferLivroD(self, id):
        banco1 = BancoD()
        banco2 = BancoO()
        
        c1 = banco1.conexao.cursor()
        comando1 = "select * from livrosD where idlivro = " + str(id) + " "
        c1.execute(comando1)
        for elemento in c1:
            nome = elemento[1]
            autor = elemento[2]
            genero = elemento[3]
        c2 = banco2.conexao.cursor()
        comando2 = "insert into livrosO(nome, autor, genero, status, opiniao, dataa) values('"+ nome +"', '"+ autor + "','"+ genero +"','" "','" "','" "')"
        c2.execute(comando2)
        comando3 = "delete from livrosD where idlivro = "+ str(id) +" "
        c1.execute(comando3)
        banco1.conexao.commit()
        banco2.conexao.commit()
        c1.close()
        c2.close()