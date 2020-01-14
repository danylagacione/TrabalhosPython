#pip3 install flask_mysqldb ---- Aula 13-01-2020 ----
#----- Referência o Mysql

# todo banco de dados(SGBD) trabalha com transações

import MySQLdb # importando a bibliotca Mysql

# Listando todos os dados existentes na tabela do BD
def listar_todos(c):
    c.execute('SELECT * FROM PESSOA')# c(cursor).executar(coloca os comandos usados no banco de dados)
    pessoas = cursor.fetchall() # coloca o cursor em uma variável (cursor.fecthall que seria pegar todos))
    for p in pessoas: # usa o for para executar todos os dados da tabela no banco de dados
        print(p)

def selecionar_ID(c, id):# para buscar pelo ID no banco de dados
    c.execute(f'SELECT * FROM PESSOA WHERE ID = {id}') 
    pessoas = c.fetchone()# listar apenas um dado
    print(pessoas)

# Buscanado o dado com uma informação (no caso pelo sobrenome)
def selecionar_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM PESSOA WHERE SOBRENOME like '{sobrenome}%'") # o Like pega determinado campo ou dado da palavra para a busca no banco de dados(% quer dizer 'tanto faz/que contenha a informação')
    for p in c.fetchall():
        print(p)

#salvar os dados de uma nova pessoa 
def salvar(cn, cr, nome, sobrenome, idade, Endereco_ID='NULL'):
    cr.execute(f"INSERT INTO PESSOA (Nome, Sobrenome, Idade, Endereco_ID )VALUES('{nome}', '{sobrenome}',{idade},{Endereco_ID})")
    cn.commit()

#alterar os dados da pessoa, pode mudar apenas um dado ex: a idade
def alterar(cn, cr, id, nome, sobrenome, idade, Endereco_ID='NULL'):
    cr.execute(f"UPDATE PESSOA SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={Endereco_ID} WHERE ID={id} ")
    cn.commit()

# #deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM PESSOA WHERE ID={id}')
    cn.commit()


conexao = MySQLdb.connect(host= '127.0.0.1', database= 'aulabd', user='root') # a conexão com o banco de dados local ou o que está na nuvem
cursor = conexao.cursor() # a conexão está na variável cursor

#listar_todos(cursor) # chamando o método e como parametro o cursor
#selecionar_ID(cursor,2) # como parametro o cursor e o número do ID da tabela que está no banco de dados
#selecionar_sobrenome(cursor,'la')
#salvar(conexao, cursor, 'Daynaries', 'KingOfdragons',18, 2)
#alterar(conexao, cursor, 7, 'Drogo', 'Kall dos Kall', 35, 2)
deletar(conexao, cursor, 3)

