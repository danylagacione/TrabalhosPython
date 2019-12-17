# Aula 27 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.


lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
print(lista is lista)
print(lista == lista)

# 2) Qual é o maior valor destas duas listas 
print(f'O valor maior da 1ª lista e da 2ª lista é: {(max(max(lista)))}')

# 3) Qual é o maior valor de cada lista
print(f'O maior valor de cada lista é {max(lista[0])} e {max(lista[1])}')

# 4) Há o número 10 dentro da lista[0]?
print('\n')
if 10 in lista[0]:
    print('Tem o número 10 na lista')
else:
    print('Não existe o nº10 na lista')

# 5) Há o número 20 dentro da lista[1]?
if 20 in lista[1]:
    print('Tem o nº20 na lista')
else:
    print('Não existe o nº20 na lista')

# 6) Quantos números da lista[0] tem dentro da lista[1]?
print('\n')
numeros_iguais = 0
for igual in lista[0]:
    for iguais in lista[1]:
        if igual == iguais:
            numeros_iguais += 1
            print(f'Tem {numeros_iguais} números iguais da lista 0 na lista 1')
        else:
            print('Não existe números iguais entre as listas')    

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
print('\n')
for indice in lista[0]:
    if indice in lista[1]:
        print(f'Existe o {indice} dentro da {lista[1]}')
    else:
        print(f'Não existe números da lista[0] dentro da lista[1]')    

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
print('\n')
soma = sum(lista[0])
for multiplica in lista[1]:
    print(soma *multiplica)
    

# 9) Faça uma divisão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
print('\n')
def numero_maior():
    if max(lista[0]) > max(lista[1]):
        print(f'O número maior da lista {max(lista[0])}')
        maior = max(lista[0])
    else:
        print(f'O número maior da lista {max(lista[1])}')
        maior = max(lista[1])
    return maior
print(numero_maior())

def numero_menor():
    if min(lista[0]) < min(lista[1]):
        print(f'O número menor da lista {min(lista[0])}')
        menor = min(lista[0])
    else:
        print(f'O número menor da lista {min(lista[1])}')
        menor = min(lista[1])
    return menor   
print(numero_menor())    

resultado = numero_maior()//numero_menor()
print(f'O resultado da divisão é: {resultado}')

if resultado in lista:
    print(f'O resultado: {resultado} está dentro da lista')
else:
    print(f'O resultado: {resultado} não está dentro da lista')

# 10) Verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
print('\n')
if max(lista[0]) in lista[1]:
    print(f' O maior número da lista[0] {max(lista[0])} está dentro da lista[1]')
else:
    print(f'O maior número da lista[0] {max(lista[0])} não está dentro da lista[1]')

if min(lista[1]) in lista[0]:
    print(f' O menor número da lista[1] {min(lista[1])} está dentro da lista[0]')
else:
    print(f'O menor número da lista[1] {min(lista[1])} não está dentro da lista[0]')    

