import sys
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37') # colocando o r na frente do endereço da pasta não é necessário mudar a barra
from Controller.squad_controller import SquadController
from Model.model_squad import Squad

squad = Squad()
squad.nome = 'Pdawan'
squad.descricao = 'estagiários'
squad.numero_pessoas = 40
squad.linguagem_backend = 'Pyhton'
squad.frameworkfrontend = 'django'

controller = SquadController()
print(controller.buscar_por_id(1))