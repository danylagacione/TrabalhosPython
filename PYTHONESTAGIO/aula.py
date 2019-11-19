#Aula 4
#---Exercício das 4 operações matemáticas básicas
# Fazer um programa que leia 2 numeros
# Realize as 4 operações matemáticas
# Imprima o resultado das operações
# Diga qual qual número é o maior dos dois números

numero1 = int (input ('digite o numero1'))
numero2 = int (input ('digite o numero2'))

resultado1 = numero1 + numero2
resultado2 = numero1 - numero2
resultado3 = numero1 * numero2
resultado4 = numero1 / numero2

print(f'soma : {numero1} + {numero2} = {resultado1}')
print(f'subtração : {numero1} - {numero2} = {resultado2}')
print(f'multiplicaçã: {numero1} * {numero2} = {resultado3}')
print(f'divisão: {numero1} / {numero2} = {resultado4}')

if numero1 < numero2:
    print(f'o numero {numero1} é o maior')
elif numero2 > numero1:
    print (f'o numero {numero2} é o maior')
else:
    print(f' os numeros {numero1} e {numero2} são iguais')
    
    
   











