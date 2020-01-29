import sys
#sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Model.model_squad import Squad
from Dao.dao_squad import SquadDao

from Model.model_sgbds import Sgbds
from Dao.dao_sgbds import SgbdsDao
from Controller.sgdbs_controller import SgbdsController

from Model.model_frontend import Frontend
from Dao.dao_frontend import FrontendDao
from Controller.frontend_controller import FrontEndController

from Model.model_backend import Backend
from Dao.dao_backend import BackendDao
from Controller.backend_controller import BackEndController

class SquadController:
    dao = SquadDao()
    model = Squad()
    
    def listar_squad(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numero_pessoas =s[3]
            squad.backend_id = s[4]
            squad.frontend_id = s[5] 
            squad.sgbds_id = s [6]        
            lista_squad.append(squad)
        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id =  s[0]
        squad.nome = s[1]
        squad.descricao = s[2]
        squad.numero_pessoas =s[3]
        squad.backend_id= s[4]
        squad.frontend_id = s[5] 
        squad.sgbds_id = s [6]     
        return squad

    def salvar(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        return self.dao.alterar(squad)
        

    def deletar(self, id):
        self.dao.deletar(id)




