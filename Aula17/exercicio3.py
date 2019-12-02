# Faça um programa que leia um número inteirode 1 a 100 no teclado e
# mostre se você acertou ou 
# o número digitado é maior ou menor.
# Quando você acertar o programa deve ser finalizado

from random import randint
aleatorio = randint (1,10)
tentativas = 0


while True:
    n = int (input ('Digite o número'))
    tentativas = tentativas +1
    if n < aleatorio:
        print ('O número digitado é menor, TENTE NOVAMENTE')
        continue
    elif n > aleatorio:
        print ('O número digitado é maior, TENTE OUTRA VEZ')
        continue        
    elif n == aleatorio:
        print ('PARABÉNS !!! Você tentou = ',tentativas)
        break


# Outra maneira de ser resolvido:

while not numero == aleatorio:
    numero = int (input('Digite um numero:'))

