import sys
sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
#sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
import MySQLdb
from Model.model_sgbds import Sgbds
from Model.model_squad import Squad
from Controller.sgdbs_controller import SgbdsController


class SgbdsDao():
    conexao = conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_sgbds(self):
        comando_sql = f"SELECT * FROM cadastrosquad.sgbds "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_id(self,id):
        comando_sql = f"SELECT * FROM cadastrosquad.sgbds"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def salvar_sgbds(self, sgbds:Sgbds):
        comando_sql = f"INSERT INTO cadastrosquad.sgbds
        (
            nome
        ) 
        VALUES
        (
            '{sgbds_id.nome}'
        )"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        backend= self.cursor.lastrowid
        return backend
    
    def alterar_sgbds(self, sgbds:Sgbds):
        comando_sql = f"UPDATE cadastrosquad.sgbds 
            SET 
                nome = '{sgbds_id.nome}',
            WHERE id = {sgbds_id.id}
        self.cursor.execute(comando_sql)
        self.conexao.commit()   
    
    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad.sgbds WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()
             