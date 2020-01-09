from flask_mysqldb import MySQLdb
from contextlib import closing

__dados = {'host': "mysql.topskills.study",
        'database': 'topskills01',
        'user': 'topskills01',
        'passwd': 'ts2019',
        'port': 3306}

def cadastrar (nome, idade, telefone):
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute (f"INSERT INTO topskills01.danielilagacione(nome, idade, telefone)VALUES('{nome}',{idade}');")
        conn.commit()

def consultarAll():
    with closing(MySQLdb.connect(**__dados)) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM danielilagacione')
        print('\nSó uma linha: ', cursor.fetchone())
        print('\nVárias linhas',cursor.fetchall())

for i in range (3):
    nome = input('Digite Nome:')
    idade = int(input('Digite a idade:'))
    telefone = int(input('Digite o telefone:'))
    cadastrar(nome, idade)

consultarAll()             
