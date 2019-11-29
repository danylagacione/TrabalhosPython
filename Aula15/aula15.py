#---Aula 15 28-11-2019
#--- Manipulação de arquivos

# arquivo = open ('aula15.txt','a') 
# arquivo.write('Voltolini Turismo\n')
# arquivo.close()

# arquivo = open ('aula15.txt','r') 
# for linha in arquivo:
#     print (linha)
# arquivo.close()

#-- Exercicio
# name = (input ('Digite o nome completo:'))
# arquivo = open ('exercicioex.txt', 'r')
# arquivo.write (name+'\n') # +\n pula a linha, o mesmo que '\n'. OU pode ser feito dessa maneira arquivo.write(f'{name}\n')
# arquivo.close()
 

def salvar_pessoa(pessoa_dicionario):
    arquivo = open ('exercicioex.txt', 'a')
    arquivo.write (f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('exercicioex.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0], 'sobrenome':lista_linha[1], 'idade':lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista

nome = (input ('Digite o nome:'))
sobrenome = (input ('Digite o sobrenome:'))
idade = int (input ('Digite a sua idade:'))

# pessoa = {'nome':nome, 'sobrenome':sobrenome, 'idade':idade} #f'{name}; {sobrenome}; {idade}'
# salvar_pessoa(pessoa)
for p in ler():
    print(f"{p['nome']} - {p['sobrenome']} - {p['idade']}")


#+\n pula a linha, o mesmo que '\n'. OU pode ser feito dessa maneira arquivo.write(f'{name}\n)
