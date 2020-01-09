#--- Banco de dados 08-01-2020

# SGBD - Sistema Gerenciador de Banco de Dados
# Mysql, Sqlserver...

# Mysql "=MariaDb
#---- No sql o = é comparação, o sinal de diferente é <>
#---- Significado de  CRUD:
#   C = create - inserir/salva - comando INSERT
#   R = read- Ler/Listar - comando SELECT
#   U = update- Alterar - comando UPDATE
#   D = delete- Apagar - comando DELETE
#
#-- O Select- lista/seleciona os dados da tabela no BD, ex: select * from Pessoa( o * seleciona todos os dados da tabela)
#    (pessoa é o nome da tabela)
#    caso queira selecionar somente uma informação exemplo o sobrenome fica select sobrenome from Pessoa.
#
#----Para inserir um novo dado na tabela é:
# Insert into Pessoa 
# ( 
#   Nome
#  ,sobrenome
#  ,idade 
# )
# Values (quais oa valores que quer inserir a tabela)
# (
#   'Tavinho'(tem que colocar com aspas simples '')
#   'Honda'
#   ,15
# )
#--- Quando deseja alterar/mudar a informação da tabela:
# UPDATE danielilagacione - seleciona a tabela que quer mudar
#	SET telefone = 02030405 - mudando o dado da tabela que deseja alterar
#	WHERE id = 1 - qual a pessoa/linha da tabela que vai ser alterado
# 
