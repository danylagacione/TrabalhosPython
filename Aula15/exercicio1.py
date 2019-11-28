#--- Exercício Cerveja Aula15 - 28-11-2019

# arquivo = open ('tipocerva.txt', 'x')
# arquivo.write = ('cerveja\n')



def cerveja(cerva_dicionario):
    arquivo = open('tipocerva.txt','a')
    arquivo.write(f"{cerva_dicionario['marca']};{cerva_dicionario['tipo']};{cerva_dicionario['teor']}\n")
    arquivo.close()

def ler():
    lista = []
    arquivo = open('tipocerva.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0], 'tipo':lista_linha[1], 'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista

marca = input('Digite a marca : ')
sobrenome = input('Digite o tipo da cerveja: ')
teor = float (input('Digite o teor alcoolico:'))
cerveja = {'marca':lista_linha, 'tipo':lista_linha, 'teor':lista_linha}
salvar_cerveja    

for k in ler():
    print(f"{k['marca']} - {k['tipo']} - {k['teor']}")






