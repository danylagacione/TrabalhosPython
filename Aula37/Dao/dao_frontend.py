import sys
sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
#sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
import MySQLdb
from Model.model_frontend import Frontend
from Controller.frontend_controller import FrontEndController
from Dao.dao_squad import SquadDao


class FrontendDao():
    conexao = conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_frontend(self):
        comando_sql = f"SELECT * FROM cadastrosquad.frontend "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self,id):
        comando_sql = f"SELECT * FROM cadastrosquad.frontend"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def salvar_frontend(self, frontend:Frontend):
        comando_sql = f"INSERT INTO cadastrosquad.frontend
        (
            nome
        ) 
        VALUES
        (
            '{frontend_id.nome}'
        )"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        backend= self.cursor.lastrowid
        return backend
    
    def alterar_frontend(self,frontend:Frontend):
        comando_sql = f"UPDATE cadastrosquad.frontend 
            SET 
                nome = '{frontend_id.nome}',
            WHERE id = {frontend_id.id}
        self.cursor.execute(comando_sql)
        self.conexao.commit()   
    
    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad.frontend WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
             