import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
import MySQLdb
from Model.model_squad import Squad
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
            framework_frontend 
            )
            
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numero_pessoas},
            '{squad.linguagem_backend}',
            '{squad.framework_frontend}'
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
            linguagem_backend = '{squad.linguagem_backend}',
            framework_frontend = '{squad.framework_frontend}'
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
