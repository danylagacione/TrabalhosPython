#---Aula 9 19-11-2019
#---Crie um programa que:
#--- 1- Leia dois números inteiros
#--- 2- Calcule a soma ente dois numeros atraves de um metodo
#--- 3- Calcule a subtração ente dois numeros atraves de um metodo
#--- 4- Calcule a multiplicação ente dois numeros atraves de um metodo
#--- 5- Calcule a divisão inteira ente dois numeros atraves de um metodo
#--- 6- Calcule a divisão fracionada ente dois numeros atraves de um metodo
#--- 7- Calcule o resto da divisão ente os dois numeros atraves de um metodo
#--- 8- Calcule a raiz ente dois numeros atraves de um metodo
#--- 9- Separa os metodos em outro arquivo


from calculo_metodo import soma, subtracao, multiplicacao, divisaointeira, divisaofracionada, resto, raiz


numero1 = int (input ('digite o numero1:'))
numero2 = int (input ('digite o numero2:'))

resultadosoma= soma(numero1, numero2)
print (resultadosoma)

resultadosubtracao = subtracao(numero1, numero2)
print (resultadosubtracao)

resultadomultiplicacao = multiplicacao(numero1, numero2)
print (resultadomultiplicacao)

resultadodivisaointeira = divisaointeira(numero1 ,numero2)
print (resultadodivisaointeira)

resultadodivisaofracionada = divisaofracionada(numero1, numero2)
print (resultadodivisaofracionada)

resultadoresto = resto(numero1 , numero2)
print (resultadoresto)

resultadoraiz = raiz(numero1, numero2)
print (resultadoraiz)

