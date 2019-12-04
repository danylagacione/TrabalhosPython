# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )

cabecalho =  cerveja[0]

dados = cerveja[1:]
for dados_cerveja in dados:
    for i in range (4):
        print (f'{cabecalho[i]} {dados_cerveja[i]}')
         

# for c in cerveja:
#     print (f'O marca da cerveja é:{cerveja[1][0]} do tipo {cerveja[1][1]} o IBU é:{cerveja[1][2]} e o preço é R$: {cerveja[1][3]}')


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

def recebe (cerveja):
    cabecalho = cerveja[0]# separar o cabecalho da tupla
    dados = cerveja[1:] # separar os dados da tupla
    lista_cerveja = [] # iniciar uma lista para receber os dados
    for dados_cerveja in dados: #FOR par a quebrr os dados gerando o dicionário para armazenar os dados
        dicionario = {cabecalho[0]:dados_cerveja[0],cabecalho[1]:dados_cerveja[1], cabecalho[2]:dados_cerveja[2], cabecalho[3]:dados_cerveja[3]}
        lista_cerveja.append(dicionario) # adiciona o dicionario na lista
    return lista_cerveja #retornando a lista para o programa
print(recebe(cerveja))        
[
    (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )]





