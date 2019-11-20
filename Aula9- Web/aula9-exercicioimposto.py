# Aula 9 19-11-2019
#-- Resolução exerício3 aula 3 


#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRF - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido


print('='*50, '\n')

# nome_completo = input('Digite seu nome completo:')
# cpf = input('Digite seu cpf:')
# num_registro = int( input('Digite seu registro:') )
# cargo = input('Digite seu cargo:')

salario = float( input('Digite seu salario:') )

inss = calculo_inss(salario)
irrf = calculo_irrf(salario, inss)

salario_liquido = salario - inss - irrf
print(f'Inss: {inss}')
print(f'Irrf: {irrf}')
print(f'Seu salário liquido é {salario_liquido}')

 if(salario>0 and salario <= 1751.81):
        inss = salario * 0.08
    elif (salario >1751.81 and salario<=2919.72 ):
        inss = salario * 0.090
    elif (salario >2919.72 and salario<=5839.45 ):
        inss = salario * 0.11
    else:
        inss = 642.34
        
irrf = 0
    if(salario>1903.98 and salario <= 2826.65):
        irrf = (((salario - inss) * 0.075)-142.80)
    elif (salario >=2826.66 and salario<=3751.05 ):
        irrf = (((salario - inss) * 0.15)-354.80)
    elif (salario >=3751.06 and salario<=4664.68 ):
        irrf = (((salario - inss) * 0.225)-636.13)
    elif(salario > 4664.68):
        irrf = (((salario - inss) * 0.275)-869.36)
        
#-- os 2 blocos de códigos (if, elif e else) podem ser colocados em método (def + o que quer chamar + nome para o metodo).

print( '\n'*2,'='*50)



