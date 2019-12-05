# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igual a 18 anos

def dados_pessoa():
        nome = pess[0]
        telefone = pess[1]  # colocando os dados em variáveis
        email = pess[2]
        idade = pess[3]
        lista= [] # cria uma lista vazia, para depois ser adicionado dados/itens dentro dela
        for i in range(len(idade)): # usa o for range e len para ler todos os dados dentro da lista que tem a idade
                if int (pess[3][i])>= 18: #verifica se a pessoa é maior ou = a 18 anos, caso seja, essa pessoa/dados será atribuido ao dicionário
                        dicionario = {'nome':nome[i], 'telefone':telefone[i], 'email':email[i], 'idade':idade[i]} #criando o dicionário
                        lista.append(dicionario) # está adicionao o dicionario dentro da lista vazia criada anteriormente
        return lista# retorna a lista com os dados/itens inseridos nela
print (dados_pessoa()) # e por último chama o a função/método                      


#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())

print('\n')
for i in dados_pessoa ():
        print(i)

#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)

print('\n')
for dados in (dados_pessoa()):
        print (f'Informações pessoais:{dados}')
