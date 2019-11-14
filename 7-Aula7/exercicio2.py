#--- Exercício 2 - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: nome, posição, numero, pernaboa
#--- Crie um dicionário para armazenar os dados
#--- Imprima todos os joogadores e seus dados


lista_jogadores = []

for i in range (1,3):
    jogador = {}
    jogadores= {'nome': '', 'posicao': '', 'numero':'', 'pernaboa':''}
    jogadores['nome'] = input ('digite o nome:')
    jogadores['posicao'] = input ('digite a posicao:')
    jogadores['numero'] = int (input ('digite o numero:'))
    jogadores['pernaboa'] = input ('digite a pernaboa:')
    lista_jogadores.append(jogadores)
    
print ('\m')
# print (lista_jogadores)    

for i in lista_jogadores:
    print (i['nome'], i['posicao'], i['numero'], i['pernaboa'])