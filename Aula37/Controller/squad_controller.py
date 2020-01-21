from Model.model_squad import Squad
from Dao.squadDao import SaquadDao


class SquadController:
    dao = squadDao()
    
    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            Squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numeropessoas =s[3]
            squad.linguagemBackEnd = s[4]
            squad.frameworkFrontEnd = s[5]         
            lista_squad.append(squad)
        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        Squad = Squad()
            squad.id =  s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numeropessoas =s[3]
            squad.linguagemBackEnd = s[4]
            squad.frameworkFrontEnd = s[5] 
        return squad

    def salvar(self, squad:Squad):
        squad.id = self.squad_controller.salvar(salvar)
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.squad_controller.alterar(salvar)
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)