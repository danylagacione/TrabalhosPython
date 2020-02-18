#===== Aula 18-02-2020

# ----Testes em Python ----

# Verificação de determinada condição é verdadeira
assert True # tem que ser tru, pois essa é a verificação que ele faz
assert (10 == 10)
assert (10 > 5)
assert (' Danieli' != 'Lagacione')

def soma (n1, n2):
    resultado = n1 + n2
    return resultado

def multiplicao(n1, n2, n3=1): # n3=1 colocando dessa maneira, o n3 fica como parâmetro opcional(valor defult)
    return n1 * n2 * n3

def checar_naioridade(idade):
    if idade >= 18:
        return True
    else:
        return False
# Teste de resultado dos métodos soma e multiplicação
assert soma (5,10) == 15 # testando métodos  soma
# Teste de método de multiplicação com arguento opcional
assert multiplicao(2,4,6) == 48
# Teste de método com a condição if
assert checar_naioridade(18) == True
#Teste de método com a condição if 2
assert checar_naioridade(19) == True
# Teste de método com a condição else
assert checar_naioridade(17) == False




