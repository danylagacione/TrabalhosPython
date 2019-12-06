# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um programa que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.
controle = 'n'
while controle != 's':
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))            
        print(f'o resultado da soma é {n1} e {n2} = {n1 + n2}')
        print(f'o resultado da multiplicação é {n1} e {n2} = {n1 * n2}')
        print(f'o resultado da divisão é {n1} e {n2} = {n1 / n2}')
        print(f'o resultado da subtração é {n1} e {n2} = {n1 - n2}')
    
        controle = input ("Digite 's' para sair:")

# while True: # Exemplo de como usar o try e except
#     try:
#         print('Passou1')
#         numero = int(input('Digite um numero:'))
#         print('Passou2')
        
#     except ValueError:

#         print('Voce digitou o número errado animal!')

#     else:
#         print('FIM!')
#         break        
#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# n = -1
# while n!= 0:
#     try:
#         n = int(input('Digite um número válido:'))
#     except:
#         print('ERRO, Digite apenas números válidos')    
#     else:
#         print ('Fim.')    

# # 4 - Faça outro tratamento de exceção para evitar que divida um numero
# # por zero.
while True:
    try:
        print('passou 1') 
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('Digite o segundo número:')) 
        print(n1/n2)
        print('passou 2')
    except (ValueError, ZeroDivisionError):
        print('Você digitou algo errado ou tentou dividir um número por zero. Digite novamente!')    
    else:
        print('FIM')
