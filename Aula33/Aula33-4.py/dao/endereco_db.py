#----- Importar biblioteca do Mysql
import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host= '127.0.0.1', database= 'aulabd', user='root')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    
    def listar_todos(self):
        comando_sql_select = "SELECT * FROM ENDERECO"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        lista_enderecos_classe = self.converter_tabela_classe(resultado)
        return lista_enderecos_classe

    def buscar_por_id(self, id):
        comando_sql_select = f"SELECT * FROM ENDERECO WHERE ID= {id}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        lista_enderecos = []
        for e in lista_tuplas:
            e1 = Endereco()
            
            e1.id = e[0]
            e1.logradouro = e[1]
            e1.numero= e[2]
            e1.complemento= e[3]
            e1.bairro = e[4]
            e1.cidade = e[5]
            e1.cep = e[6]
            lista_enderecos.append(e1)
        return lista_enderecos