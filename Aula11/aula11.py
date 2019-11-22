# Aula 11 - 21-11-2019
# Prova

#---1- Crie um programa que calcule 
# ---  o imposto ISS de um serviço de desenvolvimento de software
#---   Utilizar metodos

# print('='*50, '\n') RESOLUÇÃO EXERCÍCIO 1

# from calculoISS import valorimposto

# valor_servico = float(input ('Digite o  valor do serviço:'))
# ISS = float (input ('Digite a porcentagem da aliquota:'))

# valorimposto = valor_servico * ISS

# print(f'valor_serviço: {valor_servico} * valorimposto: {ISS} = resultado{valor_servico * ISS}')

# print('='*50, '\n')

#---2-Crie um programa que calcule 
# --- a rentabilidade anual de um investimento, baseando-se em sua rentabilidade mensal(juros compostos)
#---  a rentabilidade deve ser apresentada em % e R$
#---  Utilizar metodos

# print('='*50, '\n')

# from investimentomensal import rentabilidadeanual

# valorinicial = float(input('Digite o valor inicial:'))
# Taxa = float (input('Digite a taxa:'))

# rentanual= rentabilidadeanual (valorinicial, Taxa)

# print(f'inicial:{valorinicial} * meses a render: {Taxa} = resultado:{rentanual:.2f}')# :.2f reduz essa quantidade depois da virgula ex:561.25

# print ('='*50, '\n')

#---3-  Crie um programa para calculo de investimento
#       solicitar o valor a ser investido no Tesouro Selic
#       quantas cotas deseja comprar
#       (considerar valor do tesouro Selic Hoje)
#       calcular o valor total até o vencimento do titulo

#valor selic 10.410,00
#taxa selic 5.00+0.02 ao ano
#titulo dividido por cotas 100 ou 0,01
#vencimento 01/03/2025

from tesouroselic import rentabilidade

# valorinvestido= float (input('Digite o valor a ser investido:'))
cotas= float(input ('Digite quantas cotas deseja adquirir:'))
# taxaselic = float(input('Digite valor da taxa:'))
 
# rentabilidademensal = rentabilidade (valorinvestido, cotas, taxaselic)
# print (f'O valor investido foi:{valorinvestido}, \n Cotas adquiridas: {cotas},\n Rentabildade do investimento:{rentabilidademensal:.2f}')



#---4-
#---5-









