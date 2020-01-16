import sys
sys.path.append('C:/Users/900134/Documents/TrabalhosPython/Aula33/Aula33-4.py')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)