from flask import request

from Aula55.controller.base_controller import BaseController
from Aula55.dao.autor_dao import AutorDao
from Aula55.model.autor import Autor

class AutorController(BaseController):
    def __init__(self):
        dao = AutorDao()
        super().__init__(dao)

    def post(self):
        return super().post(self.carrega_parametros())

    def put(self, id):
        model = self.carrega_parametros()
        model.id = id
        return super().put(model)

    def carrega_parametros(self):
        self.model = Autor()
        self.pseudonimo = request.json['pseudonimo']
        self.descricao = request.json['descricao']
        self.pessoa_id = request.json['pessoa_id']
        return self.model