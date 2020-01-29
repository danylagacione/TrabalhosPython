import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Dao.dao_sgbds import SgbdsDao
from Model.model_sgbds import Sgbds

class SgbdsController:
    dao = SgbdsDao()
        
    def listar_sgbds(self):
        return self.dao.listar_sgbds

    def buscar_id_sgbds(self, id):
        return self.dao.buscar_id_sgbds

    def salvar_sgbds(self, sgbds:Sgbds):
        return self.dao.salvar(sgbds)

    def alterar_sgbds(self, sgbds:Sgbds):
        return self.dao.alterar(sgbds)

    def deletar_sgbds(self, id):
        self.dao.deletar(id)