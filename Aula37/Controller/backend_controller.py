import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')

from Dao.dao_backend import BackEndDao
from Model.model_backend import BackEnd

class BackEndController:
    dao = BackEndDao()
        
    def listar_backend(self):
        return self.dao.listar_backend()

    def buscar_id_backend(self, id):
        return self.dao.buscar_id_backend

    def salvar_backend(self, backend:BackEnd):
        return self.dao.salvar_backend(backend)

    def alterar_backend(self, backend:BackEnd):
        return self.dao.alterar_backend(backend)

    def deletar_backend(self, id):
        self.dao.deletar_backend(id)