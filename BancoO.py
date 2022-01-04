import sqlite3

#Lista de livros obtidos
class BancoO:
    def __init__(self):
        self.conexao = sqlite3.connect("bancoO.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        #executa um comando SQL
        #nesse caso cria uma tabela
        c.execute(
            """
            create table if not exists livrosO(
                idlivro integer primary key autoincrement,
                nome text,
                autor text,
                genero text,
                status text,
                opiniao text,
                dataa text
            )
            """
        )
        self.conexao.commit()
        c.close()