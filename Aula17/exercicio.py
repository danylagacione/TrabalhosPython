# 1 - Faça um menu interativo que tenha: Cadastro de banda, cadastro do album, cadastro da música e sair.
# O menu deve ser executado até que se escolha a opção sair.
# Cada opção deve ser mostrada
# Quando selecionado a opção sair, deverá aparecer na tela as informações das bandas cadastradas, album e músicas.


lista_banda = []
lista_album = []
lista_musica = []

menumusica = '''

####################################################################
#                Menu Seleção de Músicas                           #
####################################################################

1 - Cadastrar Banda
2 - Cadastrar Album
3 - Cadastrar Música
4 - SAIR

Digite a opção desejada: '''


opcao = input(menumusica)

while True:
    opcao = input(menumusica)
    if opcao == '1':
        lista_banda.append (input ('Digite o nome da Banda:'))
    elif opcao == '2':
        lista_album.append (input ('Digite o nome do album:'))
    elif opcao == '3':
        lista_musica.append (input ('Digite o nome da Música'))
    elif opcao == '4':
        print('SAIR')
        print (f'Lista de Bandas: {lista_banda}\nLista de Albuns:{lista_album}\nLista de Músicas:{lista_musica}') 
        break
    else:
        print ('Opção inválida')
          



        
    
