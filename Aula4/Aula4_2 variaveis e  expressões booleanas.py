#Aula 4_2 13-11-2019
#Boleanas

#---- Variável booleana simples com True ou False
validador = False
#---- Substituição do valor  inicial
validador = True

#----- Criação de variável booleana através de expressão de igualdade
idade = 18
validador = ( idade == 18 )
print (validador)
#----- Criação de variável booleana através de expressão dda diferença
validador = ( idade != 18 )
print (validador)
#----- Criação de variável booleana através de expressão de maior
validador = ( idade > 18 )
print (validador)
#----- Criação de variável booleana através de expressão de menor
validador = ( idade < 18 )
print (validador)
#----- Criação de variável booleana através de expressão de maior e igual
validador = ( idade >= 18 )
print (validador)
#----- Criação de variável booleana através de expressão de menor e igual
validador = ( idade <=18 )
print (validador)

#----- Criação de variável booleana através de expressão de negação
validador = not True
validador = not False

sorteado = 'Marcela'

#----- Criação de variável booleana através de duas expressões e operador E
validador = ( sorteado=='Matheus' and sorteado== 'Marcela' )
#------Criação de variável booleana através de duas expressões e operador OU
validador = ( sorteado=='Matheus' or sorteado== 'Marcela')

