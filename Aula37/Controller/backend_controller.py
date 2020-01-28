import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Dao.squad_dao import SquadDao
from Model.squad_model import Squad
from Dao.dao_backend import BackEndDao
from Model.model_backend import BackEnd

class BackEndController:
    dao = BackEndDao()
        
    def listar_backend(self):
        # lista_backend = []
        # lista_tuplas = self.dao.listar_backend()
        # for s in lista_tuplas:
        #     squad = Squad()
        #     squad.id = s[0]
        #     squad.nome = s[1]
        #     lista_backend.append(squad)
        # return lista_backend
        return self.dao.listar_backend()

    def buscar_id_backend(self, id):
        # s = self.dao.buscar_por_id(id)
        # squad = Squad()
        # squad.id = s[0]
        # squad.nome = s[1]
        # return squad
        return self.dao.buscar_id_backend

    def salvar_backend(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar_backend(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar_backend(self, id):
        self.dao.deletar(id)

#  def listar_todos(self):
#         return self.dao.listar_todos()

#     def buscar_por_id(self, id):
#         return self.dao.buscar_por_id(id)

#     def salvar(self, linguagemBackend:LinguagemBackend):
#         return self.dao.salvar(linguagemBackend)

#     def alterar(self, linguagemBackend:LinguagemBackend):
#         self.dao.alterar(linguagemBackend)

#     def deletar(self, id):
#         self.dao.deletar(id)        