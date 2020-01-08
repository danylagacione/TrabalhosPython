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
#    caso queira selecionar somente uma informação exemplo o sobrenome fica select sobrenome from Pessoa,
# Para inserir um novo dado na tabela é:
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
# # Ferramenta beaver