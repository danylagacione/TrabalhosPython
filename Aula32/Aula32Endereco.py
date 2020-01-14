import MySQLdb 

def listar_endereco(c):
    c.execute('SELECT * FROM ENDERECO')
    enderecos = cursor.fetchall() 
    for ed in enderecos: 
        print(ed)

def selecionar_ID_endereco(c, id):
    c.execute(f'SELECT * FROM ENDERECO WHERE ID = {id}') 
    enderecos = c.fetchone()
    print(enderecos)

def selecionar_logradouro(c, logradouro):
    c.execute(f"SELECT * FROM ENDERECO WHERE LOGRADOURO like '{logradouro}%'") 
    for ed_logradouro in c.fetchall():
        print(ed_logradouro)

def salvar_endereco(cn, cr, logradouro, numero, complemento, bairro, cidade, CEP):
    cr.execute(f"INSERT INTO ENDERECO (logradouro, numero, complemento, bairro, cidade, CEP) VALUES('{logradouro}', '{numero}','{complemento}','{bairro}', '{cidade}','{CEP}')")
    cn.commit()


def alterar_endereco(cn, cr, id, logradouro, numero, complemento, bairro, cidade, cep):
    cr.execute(f"UPDATE ENDERECO SET LOGRADOURO='{logradouro}',NUMERO='{numero}',COMPLEMENTO='{complemento}',BAIRRO='{bairro}',CIDADE='{cidade}',CEP='{cep}' WHERE ID={id} ")
    cn.commit()

def deletar_endereco(cn, cr, id):
    cr.execute(f'DELETE FROM ENDERECO WHERE ID={id}')
    cn.commit()


conexao = MySQLdb.connect(host= '127.0.0.1', database= 'aulabd', user='root')
cursor = conexao.cursor()

#listar_endereco(cursor) 
#selecionar_ID_endereco(cursor, 2)
#selecionar_logradouro(cursor, 'Rua')
salvar_endereco(conexao, cursor, 'Rua do amanhã', '20B', 'Apto 123', 'Bairro','Blumenau', '456789')
#alterar_endereco(conexao, cursor, 2, 'Rua definida','20c', 'Casa da Árvore', 'Área Sul','Floresta Encantada', '444555666')  
#deletar_endereco(conexao, cursor,3)
