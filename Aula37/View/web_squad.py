from flask import Flask, render_template, request, redirect
import sys
#sys.path.append(r'C:\Users\Dell\Documents\TrabalhosPython\Aula37')
sys.path.append(r'C:\Users\900134\Documents\TrabalhosPython\Aula37')
from Model.model_squad import Squad
from Controller.squad_controller import SquadController
from Controller.frontend_controller import FrontEndController
from Controller.backend_controller import BackEndController
from Controller.sgdbs_controller import SgbdsController

app = Flask(__name__)
squad_controller = SquadController()
nome = 'Cadastros Squad'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    front = frontEndController.listar_frontend()
    back = BackEndController.listar_backend()
    sgdbs = SgbdsController.listar_sgbds()
    return render_template('listar.html', titulo_app = nome, lista = squad, lista1 = front, lista2= back, lista3= sgdbs)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    front = frontEndController.listar_frontend()
    back = BackEndController.listar_backend()
    sgdbs = SgbdsController.listar_sgbds()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad, lista1 = front, lista2= back, lista3= sgdbs)


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
    squad.linguagem_backend = request.args['linguagem_backend']
    squad.framework_frontend = request.args['framework_frontend']
      
    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')
    
app.run(debug=True)
