#====Flask Restful==== Aula dia 28-01-2020 e 29-01-2020 (Restful-biblioteca do flask para APIs)

from flask import Flask
from flask_restful import Api
from Controllers.cerveja_controller import CervejaController

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')

@app.route('/')
def inicio(): #pega a string e retorna um html(simples)
    return 'Bem vindo a API'

app.run(debug=True, port=80) # a porta 5000 é para produção (caso não de erro ou não funcione) usar uma porta alternativa)


