#2 -
# Mercado Tech ----
# Solicitar nome do funcionário
# Solicitar idade
# Informar se o funcionário pode adquirir produtos alcoolicos


#3 -
# Cadastro produto Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolicos e Não alcoolicos)
# Exibir cadastro

print ('Mercado Tech')

funcionário = input('informar seu nome e sobrenome:')
idade = int (input ('informar sua idade:'))

if (idade) <= 17:
    print ('Não está autorizado a adquirir produtos alcolicos')
else:
    print('Autozizado a adquirir produtos alcoolicos')



print ('cadastro de produtos')

produto = input ('informar o produto:')
categoria = input ('alcoolico ou não alcoolico:')
print (f'item: {produto} definição: {categoria}')