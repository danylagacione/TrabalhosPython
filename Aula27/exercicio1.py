# Aula 27 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint


lista1 = lista_simples_int(randint (5,100))
lista2 = lista_simples_int(randint (5,75))
lista3 = lista_simples_int(randint (5,70))

print(len(lista1))
print(len(lista2))
print(len(lista3))
# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print (f'Esse é o tamanho da lista: {len(lista1)}')

# 1.2) Qual é o maior valor da lista2?
print(f'O maior valor é : {max(lista2)}')

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(f'O menor número é {min(lista2)}')
print (f'O maior valor é {max(lista2)}')
print(f'A soma valor maior e menor é: {max(lista2) + min(lista2)}')

# 1.4) Qual é a média aritmética da lista1?
print (f'Esse é o tamanho da lista: {sum(lista1) / len(lista1)}')


# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f'A soma da lista 1 é: {sum(lista1)}')
print(f'A soma da lista 2 é: {sum(lista2)}')
print(f'A soma da lista 3 é: {sum(lista3)}')
print(f'A soma das três listas acima é: {sum(lista1) + sum(lista2) + sum(lista3)}')
print('\n')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for valor in lista1:
    print (f'O valor da lista 1 é:{valor}')
print('\n')    

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
print('\n')
lista_posicao = [5,9,10,25]
listas_listas = [lista1, lista2, lista3]
for posicao in lista_posicao:
    n = 0
    for i in listas_listas:
        n += 1
        try:
            print(f'O valor da lista {n} é {(i[posicao])}')
        except IndexError:
            print(f' Erro de lista {n} posição {posicao}')

# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
print('\n')
if len(lista1) > len(lista2) and len(lista3):
    print(f' A lista 1 é maior, tem {len(lista1)} itens')
elif len(lista2) > len(lista1) and len(lista3):
    print (f'A lista 2 é maior, tem {len(lista2)} itens')
elif len(lista3) > len(lista1) and len(lista2):
    print(f'A lista 3 é maior, tem {len(lista3)} itens')       
print ('\n')

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
# def menores():
#     if min(lista1) < min(lista2) and min(lista3):
#         print(f'O menor valor da lista 1 é {min(lista1)}')
#     elif min(lista2) < min(lista1) and min(lista3):
#         print(f'O menor valor da lista 2 é {lista2}')
#     elif min(lista3) < min(lista2) and min(lista1):
#         print(f'O menor valor da lista 3 é {lista3}')
#     return menores    
# menores()
# maiores = max(lista1) + max(lista2) + max(lista3)
# print (maiores)


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
print (f'{max(lista1)} {max(lista2)} {max(lista3)}')
