# Aula7 - 14-11-2019
# Dicionários

#--- Criação de uma variável tipo dicionário 
dicionario = { 'nome': 'Danieli', 'sobrenome': 'Lagacione' }
#--- Impressão de um dicionário completo
print (dicionario)
#--- Impressão de um dos dados do dicionário através da chave
print (dicionario['sobrenome'])

#--- Criação de dicionário através de variávieis de tipos distintos
nome = 'Mirella'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/ len(lista_notas)
situação = 'reprovado'
if media >=7:
    situação = 'aprovado'
dicionario_alunos = {'nome':nome, 'lista_notas':lista_notas, 'media': media, 'situação':situação}
#--- Impressão de dados do dicionário através de suas chaves
print (f"{dicionario_alunos ['nome']} - {dicionario_alunos['situação']}")


#--- Criação de um dicionário com valores padrão e alteração do valor posterior a criação
dicionario_bandas = ['nome': '']
#--- Alteração do valor através da chave
dicionario_bandas = ['nome'] = 'calipso'
dicionario_bandas = ['nome'] ='Djavu'
print (dicionario_bandas)

#--- Criação de um dicionario e adição de uma nova chave após a criação
dicionario = {'nome': 'Danieli', 'sobrenome:' 'Lagacione'}
dicionario  ['sobrenome'] = 'Lagacione'
#--- Adição de nova chave/valor ao dicionário existente
dicionario ['CPF'] = '395.114.018-66'

#--- Criação de um dicionário com dados de uma pessoa e através do laço de repetição adicinar em lista
lista_pessoas = []
for i in range (1,11):
    dicionario_pessoa = {'nome': '', 'sobrenome': '', 'CPF':'', 'RG':''}
    dicionario_pessoa['nome']= input ('digite o nome:') 
    dicionario_pessoa['sobrenome']= input ('digite o sobrenome:')
    dicionario_pessoa['CPF']= input ('digite o CPF:')
    dicionario_pessoa['RG']= input ('digite o RG:')
    lista_pessoas.append(dicionario_pessoa)