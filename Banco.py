import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        #executa um comando SQL
        #nesse caso cria uma tabela de dados dos casos
        c.execute(
            """
            create table if not exists usuarios(
                idusuario integer primary key autoincrement,
                nome text,
                telefone text,
                email text,
                tipo text,
                cidade text,
                bairro text,
                cep text,
                idade text,
                senha text
            )
            """
        )
        self.conexao.commit()
        c.close()