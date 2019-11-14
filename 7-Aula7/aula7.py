# Aula7 - 14-11-2019
# Dicionários

# lista = []
# dicionario = { 'nome': 'Danieli', 'sobrenome': 'Lagacione' }
# print (dicionario)
# print (dicionario['sobrenome'])

# nome = 'Mirella'
# lista_notas = [10,20,50,70]
# media = sum(lista_notas)/ len(lista_notas)
# situação = 'reprovado'
# if media >=7:
#     situação = 'aprovado'
# dicionario_alunos = {'nome':nome, 'lista_notas':lista_notas, 'media': media, 'situação':situação}

# print (f"{dicionario_alunos ['nome']} - {dicionario_alunos['situação']}")



# dicionario_bandas = ['nome': '']
# dicionario_bandas = ['nome'] = 'calipso'
# dicionario_bandas = ['nome'] ='Djavu'

# print (dicionario_bandas)

# dicionario = {'nome': 'Danieli', 'sobrenome:' 'Lagacione'}
# dicionario  ['sobrenome'] = 'Lagacione'
# dicionario ['CPF'] = '395.114.018-66'

lista_pessoas = []
for i in range (1,11):
    dicionario_pessoa = {'nome': '', 'sobrenome': '', 'CPF':'', 'RG':''}
    dicionario_pessoa['nome']= input ('digite o nome:')
    dicionario_pessoa['sobrenome']= input ('digite o sobrenome:')
    dicionario_pessoa['CPF']= input ('digite o CPF:')
    dicionario_pessoa['RG']= input ('digite o RG:')
    lista_pessoas.append(dicionario_pessoa)