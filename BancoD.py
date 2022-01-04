import sqlite3
#Lista de livros desejados
class BancoD:
    def __init__(self):
        self.conexao = sqlite3.connect("bancoD.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        #executa um comando SQL
        #nesse caso cria uma tabela
        c.execute(
            """
            create table if not exists livrosD(
                idlivro integer primary key autoincrement,
                nome text,
                autor text,
                genero text,
                site text,
                valor text,
                dataa text
            )
            """
        )
        self.conexao.commit()
        c.close()