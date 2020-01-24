import sys
#sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
import MySQLdb
from Model.model_squad import Squad
from Model.model_backend import Backend
from Model.model_frontend import Frontend
from Model.model_sgbds import Sgbds
#from Controller.squad_controller import SquadController


class SquadDao:
    conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM cadastrosquad "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    
    def buscar_por_id(self, id):
        comando_sql = f"SELECT * FROM cadastrosquad  WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando_sql = f""" INSERT INTO cadastrosquad
        (
            nome,
            descricao,
            numero_pessoas,
            linguagem_backend,
            framework_frontend,
            fk_linguagem_backend,
            fk_framework_frontend,
            fk_sgbds 
            )
            
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numero_pessoas},
            '{squad.fk_linguagem_backend}',
            '{squad.fk_framework_frontend}',
            '{squad.fk_sgbds}'

        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        novo_squad= self.cursor.lastrowid
        return novo_squad

    def alterar(self, squad:Squad):
        comando_sql = f""" UPDATE cadastrosquad
        SET
            nome = '{squad.nome}',
            descricao = '{squad.descricao}',
            numero_pessoas = {squad.numero_pessoas},
            fk_linguagem_backend = {squad.fkbackend.id},
            fk_framework_frontend = {squad.fkfrontend.id},
            fk_sgbds = {squad.fksgbds.id}'
        WHERE id = {squad.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()


#SquadDao()
# listar_todos(conexao, cursor)
# buscar_por_id(conexao, cursor, 1)
