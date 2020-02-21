
from Aula60.ForTwo.Resolução2.embarque import embarque
from Aula60.ForTwo.Resolução2.desembarque import desembarque

from Aula60.ForTwo.Resolução2.terminal import Terminal
from Aula60.ForTwo.Resolução2.aviao import Aviao
from Aula60.ForTwo.Resolução2.local import Local
from Aula60.ForTwo.Resolução2.fortwo import Fortwo

terminal = {'descricao':'terminal', 'pessoas': ['piloto','oficial1','oficial2','chefe de serviço','comissário1','comissário2','policial','presidiario']}
aviao = {'descricao':'aviao', 'pessoas': []}

def viagem(motorista:str, passageiro:str, saida:dict, chegada:dict):

    fortwo = embarque(motorista, passageiro, saida)
    print(f"Saindo do {saida['descricao']}")
    print('Iniciando a viagem...')
    print(f"Chegando no {chegada['descricao']}")
    print('Finalizando a viagem ...')
    # alto acoplamento
    desembarque(fortwo, chegada)
    print(saida)
    print(chegada)

def viagem2(pessoa1, pessoa2, origem:Local, destino:Local):
    fortwo = Fortwo()
    if origem.saida(pessoa2):
        if origem.saida(pessoa1):
            if fortwo.set_motorista(pessoa1):
                if fortwo.set_passageiro(pessoa2):
                    fortwo.viagem(origem, destino)
                    if destino.entrada(pessoa1):
                        if not destino.entrada(pessoa2):
                            print('Não permitido6')
                    else:
                        print('Não permitido5')
                else:
                    print('Não permitido4')
            else:
                print('Não permitido3')
        else:
            print('Não permitido2')
    else:
        print('Não permitido1')


aviao1 = Aviao()
terminal1 = Terminal()

viagem2('policial','presidiário', terminal1, aviao1)
viagem2('policial','', aviao1, terminal1)
viagem2('piloto','policial', terminal1, aviao1)
viagem2('piloto','', aviao1, terminal1)
viagem2('piloto','oficial1', terminal1, aviao1)
viagem2('piloto','', aviao1, terminal1)
viagem2('piloto','oficial2', terminal1, aviao1)
viagem2('piloto','', aviao1, terminal1)
viagem2('chefe de serviço','piloto', terminal1, aviao1)
viagem2('chefe de serviço','', aviao1, terminal1)
viagem2('chefe de serviço','comissário1', terminal1, aviao1)
viagem2('chefe de serviço','', aviao1, terminal1)
viagem2('chefe de serviço','comissário2', terminal1, aviao1)

# viagem2('piloto','oficial1', terminal1, aviao1)
# viagem2('piloto','', aviao1, terminal1)
# viagem2('piloto','oficial2', terminal1, aviao1)
# viagem2('piloto','', aviao1, terminal1)
# viagem2('chefe de serviço','piloto', terminal1, aviao1)
# viagem2('chefe de serviço','', aviao1, terminal1)
# viagem2('chefe de serviço','comissário1', terminal1, aviao1)
# viagem2('chefe de serviço','', aviao1, terminal1)
# viagem2('chefe de serviço','comissário2', terminal1, aviao1)
# viagem2('chefe de serviço', '', aviao1, terminal1)
# viagem2('policial','presidiário', terminal1, aviao1)
# viagem2('piloto','', aviao1, terminal1)
# viagem2('piloto','chefe de serviço', terminal1, aviao1)
