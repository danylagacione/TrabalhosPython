#--- Exercício Cerveja Aula15 - 28-11-2019

arquivo = open ('tipocerveja.txt', 'a')
arquivo.write = ('cerveja\n')
arquivo.close ()

def salvar_cerveja(cerveja_dicionario):
    arquivo = open('tipocerveja.txt','r')
    arquivo.write(f"{cerveja_dicionario['marca']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor']}\n")
    arquivo.close()


def ler():
    lista = []
    arquivo = open('tipocerveja.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0],'tipo':lista_linha[1],'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista   
       
marca = input('Digite a marca: ')
tipo = input('Digite o tipo da cerveja: ')
teor = float (input('Digite o teor alcoolico:'))

# cerveja = {'marca':listar_linha,'tipo':listar_linha,'teor':listar_linha}
# salvar_cerveja   

for c in ler():
    print(f"{c['marca']} - {c['tipo']} - {c['teor']}")







