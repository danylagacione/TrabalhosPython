import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Dao.dao_frontend import FrontEndDao
from Model.model_frontend import FrontEnd

class FrontendController:
    dao = FrontendDao()
        
    def listar_frontend(self):
        return self.dao.listar_frontend

    def buscar_id_frontend(self, id):
        return self.dao.buscar_id_frontend

    def salvar_frontend(self, frontend:FrontEnd):
        return self.dao.salvar_frontend(frontend)

    def alterar_frontend(self, frontend:FrontEnd)):
        return self.dao.alterar_frontend(frontend)

    def deletar_frontend(self, id):
        self.dao.deletar_frontend(id)