from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900134/Documents/TrabalhosPython/Aula33/Aula33-4.py')
from controller.pessoa_controller import PessoaController

app = Flask(__name__)
pc = PessoaController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    return render_template('index.html', lista = pessoas)



app.run(debug=True) # NUNCA subir pro servidor com o debug = True (ele mostra na página web onde exatamente é que está o seu erro)
