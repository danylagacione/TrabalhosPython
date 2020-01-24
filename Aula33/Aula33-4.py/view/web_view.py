from flask import Flask, render_template 
import sys
sys.path.append('C:/Users/900134/Documents/TrabalhosPython/Aula33/Aula33-4.py')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

app = Flask(__name__) # passa o nome do arquivo
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    enderecos = ec.listar_todos()
    return render_template('index.html', lista = pessoas, listaed= enderecos) 



app.run(debug=True) 
# NUNCA subir pro servidor com o debug = True (ele mostra na página web onde exatamente é que está o seu erro)
# e ainda facilita a entrada de hacker
#=== O render template ele te possibilita retornar uma página de html, render template aponta para o index
# usando a barra na route por ser a rota principal (onde se inicia).

