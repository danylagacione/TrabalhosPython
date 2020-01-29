import sys
sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
#sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')

from Model.model_backend import  Backend
from Model.model_frontend import Frontend
from Model.model_sgbds import Sgbds

class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.backend_id = 0
        self.frontend_id = 0
        self.sgbds_id = 0
    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numero_pessoas};{self.backend_id};{self.frontend_id};
                {self.sgbds_id}'

squad = Squad() 


       
