# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00)
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante,
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

#arquivo = open ('Aula18-ListasExercicios/cadastro.txt', 'r')
# conteudo = (arquivo.read())

# linhas_do_arquivo =  conteudo.split('\n')

# print (todo_o_arquivo[0:10])

# contador = 0
# for campo in campos:
#     dicio[campo] = dados[contador]
#     i = contador + 1

#     print(f'{campos[1]}: {campos[3]}')

def ler_cadastro():
    arquivo = open ('Aula18-ListasExercicios/cadastro.txt', 'r')
    lista = []
    for pessoa in arquivo:
        pessoa = pessoas.strip().split(';')
        dicionario = {'codigo':pessoas [0], 'nome':pessoas[1],
                      'sexo':pessoas[2], 'idade':pessoas[3]}
        lista.append(dicionario)
    arquivo.close
    return lista
print (ler_cadastro())


def lista_festa (lista_de_entradas):
    lista_masculino = []
    lista_feminino = []

    for pessoas in lista_de_entradas:
        if  int(pessoa['idade']) >= 18:
            if pessoa['sexo'] == 'f':
               lista_feminino.append(pessoa)
            else:
                lista_masculino.append(pessoas)

    salvar(lista_masculino, 'masculino')
    salvar(lista_feminino, 'feminino')        
        
def salvar (lista,nome):
    arquivo = open(f'Aula18-ListasExercicios/{nome}.txt', 'a')
    for pessoa in lista:
        texto - f"{pessoa['codigo']};{pessoa['nome']}; {pessoa['sexo']};{pessoa['idade']}"
        arquivo.write(texto)
    arquivo.close() 

def consulta(lis_consulta):
    for lista_consulta in lista_consulta_funcao:
        if int (lista_consulta['codigo']) == numero:

            if lista_consulta['idade'] >=18:
                if lista_consulta['sexo'] = 'f':
                    print(f"nome:{lista_consulta['nome']} valor ingresso: R$ 15.00")
                else:
                    print (f"nome:{lista_consulta['nome']} valor ingresso: R$ 35.00") 
            else:
                print('Não pode Entrar!')           

lista1 = ler_cadastro()
lista_festa(lista1)

while True:
    a= int (input('Digite um numero:'))
    consulta(lista1,a)




