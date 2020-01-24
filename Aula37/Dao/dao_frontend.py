import MySQLdb
#from Model.model_backend import Backend
from Model.model_frontend import Frontend
# importar o controller

class FrontendDao():
    conexao = conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_linguagem(self):
        comando_sql = f"SELECT * FROM cadastrosquad.fkfrontend "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self,id):
        comando_sql = f"SELECT * FROM cadastrosquad.fkfrontend"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def salvar_frontend(self, frontend:Frontend):
        comando_sql = f"INSERT INTO cadastrosquad.fkfrontend
        (
            nome
        ) 
        VALUES
        (
            '{fk_framework_frontend}'
        )"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        backend= self.cursor.lastrowid
        return backend
    
    def alterar_frontend(self,frontend:Frontend):
        comando_sql = f"UPDATE cadastrosquad.fkfrontend 
            SET 
                nome = '{fk_framework_frontend.nome}',
            WHERE id = {fk_framework_frontend.id}
        self.cursor.execute(comando_sql)
        self.conexao.commit()   
    
    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad.fkfrontend WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
             