#===== Aula 59 dia 18-02-2020

#==== MÉTODOS =====

#---Argumentos ordenados - Métodos para uso de parâmetros ordenados
def soma (n1, n2):
    resultado = n1 + n2
    return resultado
#chamadas de metodos com argumentos nomeados
res = soma(10,20)
print(res)

#---- Argumentos nomeados - Métodos para uso de parâmetros nomeados
def subtracao(n1, n2, n3):
    resultado = n1 * n2 * n3
    return resultado
#chamadas de metodos com argumentos nomeados
res2 = subtracao (n3=10, n2=20, n3=30)
print(res2)

#--- Argumentos opcionais - Métodos para uso de parâmetros opcionais
def multiplicao(n1, n2, n3=1): # n3=1 colocando dessa maneira, o n3 fica como parâmetro opcional(valor defult)
    return n1 * n2 * n3
#chamadas de metodos com argumentos opcional
res3 = multiplicao(10,20)
print(res3)





