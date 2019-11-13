# Aula 4 11-11-2019
# Estrutura de decisão

idade = 25
#--- If simples, validação de apenas uma condição
if idade == 18:
    print ('Maior')

#------If com else,
#----- caso a condição validada pelo if não seja verdadeira,
#------o else é executado

if (idade < 18):
    print ('Menor')
else:
    print ('Maior')

#---- If com Elif e else
#--- Caso a condição validada no if seja falsa
#--- Else é  executado
if idade < 18:
    print ('Dimenor')   
elif idade ==18:
    print ('Silasco')
else:
    print ('Silasco mais ainda')

#--- If com variável booleana
#--- Em caso de variável booleana, não é necessário a validacao(==True)
#--- Pois o If ja valida o se o conteúdo da variável é True, senão vai para o Else
ativo = True
if ativo:
    print('Logar')
else:
    print('Não pode')       