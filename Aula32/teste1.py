from flask_mysqldb import MySQLdb as __MySQLdb

def listar_endereco():
    conexao = __MySQLdb.connect(host= '127.0.0.1', database= 'aulabd', user='root')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM ENDERECO')
    enderecos = cursor.fetchall() 
    for ed in enderecos: 
        print(ed)