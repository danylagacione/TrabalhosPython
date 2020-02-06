# ===Aula 53 dia 05-02-2020

# ORM
#--- (Antes criar um ambiente virtual)
# ---- SqlAlchemy
# ---- Instalação do framework
#---- pip3 intall sqlalchemy

#---- Conector Mysql
#---- Instalação do conector do Mysql
#---- pip3 install mysql-connector-python ( é o conector do mysql para o python)

# Quando importar uma biblioteca maior, exemplo o sqlalchemy tem que nomear
#       ex: import sqlalchemy as db


# alchemy faz o mapeamento da tabela/banco de dados - todas as configurações do alchemy precisa ser feita antes do
#__init___,
#===Exemplo:

# from Aula53.dao.produto_dao import ProdutoDao
# dao = ProdutoDao()
# produtos = dao.list_all()
# print(produtos)
# for p in produtos:
#     print(p)

from Aula53.dao.endereco_dao import EnderecoDao
#--- Teste de listagem dos dados de uma tabela
#--- Utilização da classe dao de produtos que utiliza uma classe base que contem os dados de acesso a base de dados
dao = EnderecoDao()
enderecos = dao.list_all()
print(enderecos)
for e in enderecos:
    print(e)
