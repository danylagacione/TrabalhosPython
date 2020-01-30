
from flask import Flask
from flask_restful import Api

from Aula41.Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa')

@app.route('/')
def iniciar():
    return 'Welcome to Controller People'

app.run(debug=True, port=4000)
