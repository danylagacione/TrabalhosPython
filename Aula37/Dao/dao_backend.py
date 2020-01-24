import MySQLdb
from Model.model_backend import Backend
# importar o controller

class BackendDao():
    conexao = conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_linguagem(self):
        comando_sql = f"SELECT * FROM cadastrosquad.fkbackend "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self,id):
        comando_sql = f"SELECT * FROM cadastrosquad.fkbackend"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def salvar_backend(self, backend:Backend ):
        comando_sql = f"INSERT INTO cadastrosquad.fkbackend
        (
            nome
        ) 
        VALUES
        (
            '{fk_linguagem_backend}'
        )"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        backend= self.cursor.lastrowid
        return backend
    
    def alterar_backend(self,backend:Backend ):
        comando_sql = f"UPDATE cadastrosquad.fkbackend 
            SET 
                nome = '{fk_linguagem_backend.nome}',
            WHERE id = {fk_linguagem_backend.id}
        self.cursor.execute(comando_sql)
        self.conexao.commit()   
    
    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad.fkbackend WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
             



