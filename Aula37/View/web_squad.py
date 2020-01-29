from flask import Flask, render_template, request, redirect
import sys
#sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Model.model_squad import Squad
from Dao.dao_squad import Squad
from Controller.squad_controller import Squad

from Model.model_backend import Backend
from Dao.dao_backend import BackendDao
from Controller.backend_controller import BackEndController

from Model.model_frontend import Frontend
from Dao.dao_frontend import Frontend
from Controller.frontend_controller import FrontEndController

from Model.model_sgbds import Sgbds
from Dao.dao_sgbds import SgbdsDao
from Controller.sgdbs_controller import SgbdsController

app = Flask(__name__)
squad_controller = SquadController()
backend_controller = BackEndController()
frontend_controller = FrontEndController()
sgdbs_controller = SgbdsController()

nome = 'Cadastros Squad'

####### WEB SQUAD ######
@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome)

@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    if id != 'None':
        squad_controller.deletar(id)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = int(request.args['id'])
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numero_pessoas = int(request.args['numero_pessoas'])
    squad.backend_id = request.args['backend_id']
    squad.frontend_id = request.args['frontend_id']
      
    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')
    
app.run(debug=True)
