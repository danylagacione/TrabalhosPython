from Model.model_backend import  Backend
from Model.model_frontend import Frontend
from Model.model_sgbds import Sgbds

class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.fk_linguagem_backend = 0
        self.fk_framework_frontend = 0
        self.fk_sgbds = 0

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numero_pessoas};{self.linguagem_backend};{self.framework_frontend};
                {self.fk_linguagem_backend};{self.fk_framework_frontend};{self.fk_sgbds}'

squad = Squad() 


       
