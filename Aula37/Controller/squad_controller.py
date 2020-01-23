import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Dao.dao_squad import SquadDao
from Model.model_squad import Squad

class SquadController:
    dao = SquadDao()
    model = Squad()
    
    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numero_pessoas =s[3]
            squad.linguagem_backend = s[4]
            squad.framework_frontend = s[5]         
            lista_squad.append(squad)
        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  s[0]
        squad.nome = s[1]
        squad.descricao = s[2]
        squad.numero_pessoas =s[3]
        squad.linguagem_backend = s[4]
        squad.framework_frontend = s[5] 
        return squad

    def salvar(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)




