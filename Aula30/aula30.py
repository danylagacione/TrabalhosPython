#--- BANCO DE DADOS 08-01-2020

# SGBD - Sistema Gerenciador de Banco de Dados
# Mysql, Sqlserver...

# Mysql "=MariaDb
#---- No sql o = é comparação, o sinal de diferente é <>
#---- Significado de  CRUD:
#   C = create - inserir/salva - comando INSERT
#   R = read- Ler/Listar - comando SELECT
#   U = update- Alterar - comando UPDATE
#   D = delete- Apagar - comando DELETE
#---- Sempre quando for abrir o MySQL, mas antes disso, fazer a conexão (estecomputador/discolocal(C)/xampp/mysql_start)
#
#-- O Select- lista/seleciona os dados da tabela no BD, ex: select * from Pessoa( O * seleciona todos os dados da tabela)
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
#-------- AULA DIA 10-01-2020 --------
#---PK(chave primária) é igual ID, pode ser o nome também, preferível que seja auto incremente(vai fazendo automático)
#---FK (chave instrangeira) quando se refere a outra tabela/apontando para outra tabela

# -----Aula dia 13-01-2020--------
# ----Ligando uma tabela a outra ex: a pessoa ao endereço: (sempre colocar todo o caminho no nome da tabela ex: aulabd.pessoa)
# From pessoa as P --nomeando a tabela pessoa como P
# join endereço as E --nomeando a tabela endereço (tabela que vai ser ligada a primeira(pode usar o inner join))
# on P.endereco_ID = E.ID 
# Outra maneira para se usar o Join:
# From pessoa as P --nomeando a tabela pessoa como P
# LEFT ou RIGHT join endereço as E --nomeando a tabela endereço 
# on P.endereco_ID = E.ID  

