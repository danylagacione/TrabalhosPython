#pip3 install flask_mysqldb
#----- Referencia o Mysql

import MySQLdb # importando a bibliotca Mysql

def listar_todos(c):
    c.execute('SELECT * FROM PESSOA')# c(cursor).executar(coloca os comandos usados no banco de dados)
    pessoas = cursor.fetchall() # coloca o cursor em uma variável (cursor.fecthall que seria pegar todos))
    for p in pessoas: # usa o for para executar todos os dados da tabela no banco de dados
        print(p)

def selecionar_ID(c, id):
    c.execute(f'SELECT * FROM PESSOA WHERE ID = {id}') 
    pessoas = c.fetchone()# listar apenas um dado
    print(pessoas)

def selecionar_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM PESSOA WHERE SOBRENOME like '{sobrenome}%'") # o Like pega determinado campo ou dado da palavra para a busca no banco de dados(% quer dizer 'tanto faz/que contenha a informação')
    for p in c.fetchall():
        print(p)

conexao = MySQLdb.connect(host= '127.0.0.1', database= 'aulabd', user='root') # a conexão com o banco de dados local ou o que está na nuvem
cursor = conexao.cursor() # a conexão está na variável cursor
#listar_todos(cursor) # chamando o método e como parametro o cursor
#selecionar_ID(cursor,2) # como parametro o cursor e o número do ID da tabela que está no banco de dados
#selecionar_sobrenome(cursor,'la')
selecionar_idade(cursor, '19')


