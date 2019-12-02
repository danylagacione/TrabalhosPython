#-- Criar um programa para o cadastro de cliente
# Para cadastro de clientes deve pedir os seguintes dados:
#Código do cliente, CPF, Nome completo,
# data de nascimento, Estado, Cidade, CEP, Bairro, Rua, numeto da casa, complemento.

# Uma funcionalidade do range colocar uma variável, mas ela tem que ser do tipo int ao invés de digitar os numeros.


def cadastro_cliente(numero_funcao):
    dados_cliente = ['Codigo do cliente','CPF', 'Nome completo',
                    'data de nascimento', 'Estado', 'Cidade', 'CEP', 
                    'Bairro', 'Rua', 'numero da casa', 'complemento']
                    
    lista = []
    
    for j in range (numero_funcao):
        dicionario = {}  

        for i in dados_cliente:
            dicionario[i] = (input (f' {i}: ')) 
        lista.append (dicionario) 
    return lista    

        
    #print (dicionario)  
    print (lista)

numero = int(input('Digite o número de cadastros:'))
lista_cadastro = cadastro_cliente(numero)

# Criar uma função para salvar em arquivo:

for cliente in lista_cadastro:
    cliente_chaves = list(cliente.keys()) #usando o KEYS você isola as chaves do seu dicionário
    for chaves in cliente_chave:


arquivo.write(f'')
arquivo.close()