import sys
sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
#sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
import MySQLdb
from Model.model_backend import Backend
from Controller.backend_controller import BackEndController

class BackendDao():
    conexao = conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_backend(self):
        comando_sql = f"SELECT * FROM cadastrosquad.backend "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self,id):
        comando_sql = f"SELECT * FROM cadastrosquad.backend"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def salvar_backend(self, backend:Backend ):
        comando_sql = f"INSERT INTO cadastrosquad.backend
        (
            nome
        ) 
        VALUES
        (
            '{backend_id.nome}'
        )"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        backend= self.cursor.lastrowid
        return backend
    
    def alterar_backend(self,backend:Backend ):
        comando_sql = f"UPDATE cadastrosquad.backend 
            SET 
                nome = '{backend_id.nome}',
            WHERE id = {backend_id.id}
        self.cursor.execute(comando_sql)
        self.conexao.commit()   
    
    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad.backend WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
             



