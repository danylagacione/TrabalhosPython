import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
import MySQLdb
import MySQLdb
#from Model.model_backend import Backend
from Model.model_sgbds import Sgbds
# importar o controller

class Sgbds():
    conexao = conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_sgbds(self):
        comando_sql = f"SELECT * FROM cadastrosquad.fksgbds "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self,id):
        comando_sql = f"SELECT * FROM cadastrosquad.fksgbds"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def salvar_sgbds(self, sgbds:Sgbds):
        comando_sql = f"INSERT INTO cadastrosquad.fksgbds
        (
            nome
        ) 
        VALUES
        (
            '{fk_sgbds}'
        )"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        backend= self.cursor.lastrowid
        return backend
    
    def alterar_sgbds(self, sgbds:Sgbds):
        comando_sql = f"UPDATE cadastrosquad.fksgbds 
            SET 
                nome = '{fk_sgbds.nome}',
            WHERE id = {fk_sgbds.id}
        self.cursor.execute(comando_sql)
        self.conexao.commit()   
    
    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad.fksgbds WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
             