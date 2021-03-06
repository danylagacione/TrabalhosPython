#======= ESTRUTURAS DE DADOS E DB Aula- 15-01-2020

#----- Importar biblioteca do Mysql
import MySQLdb

#----- Configurar a conexão
conexao = MySQLdb.connect(host= '127.0.0.1', database= 'aulabd', user='root')
#----- Salva o cursor da conexão em uma variável
cursor = conexao.cursor()

#----- Criação do comando SQL e passado para o cursor
comando_sql_select = "SELECT * FROM PESSOA"
cursor.execute(comando_sql_select)
#---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
resultado = cursor.fetchall()

#cria uma lista para armazenar os dicionarios
lista_pessoas = []
for p in resultado:
    #----- Criação do dicionario que representa uma pessoa
    dicionario_pessoa = {'Id': 0, 'Nome' : '', 'Sobrenome': '', 'Idade' : 0, 'Endereco_Id': 0}
    #--- pega cada posição da tupla e atribui a uma chave do dicionário
    dicionario_pessoa['Id'] = p[0]
    dicionario_pessoa['Nome'] = p[1]
    dicionario_pessoa['Sobrenome'] = p[2]
    dicionario_pessoa['Idade'] = p[3]
    dicionario_pessoa['Endereco_Id'] = p[4]
    lista_pessoas.append(dicionario_pessoa)

#----- Cria um arquivo e atribui a uma variável 'arquivo'
with open('Aula33/pessoas.txt','a') as arquivo: #abre e fecha o arquivo automático
    #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
    for p in lista_pessoas:
        arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")