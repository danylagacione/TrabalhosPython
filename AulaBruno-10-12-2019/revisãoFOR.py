numero_inicial = int (input('Qual número você deseja começar a somar?'))
numero_final = int (input('Agora, até qual número devemos somar?'))
total = 0 # acumulador
for numero in range(numero_inicial, numero_final+1):
    #total = total + numero
    total += numero
print(f'Total:{total}')   

total = 0
for numero in [50,51,52,53,54,55,56,57] + list(range(66,101)): 
    total += numero
print(f'Total gohorse:{total}')

texto = "Tá legal, nosso proprio split, 3 textos em uma lista"

print(texto.split(','))

def nosso_split(txt, sep):
    #return txt.split(sep)
    result = []
    count = 0
    last_sep_pos = 0
    for char in txt:
        if char == sep:
            result.append( txt[last_sep_pos:count] )
            last_sep_pos = count +1
        count += 1
    if last_sep_pos<len(txt)-1:
        result.append(txt[last_sep_pos:])

    return result

print(nosso_split(texto, ','))



print('em range')
for i in range(1, 100, 2):
    print(i)
print('esse é o i depois do for', i)
print('em lista')
for i in [1,2,3,4,5,6,7,8]:
    print(i)

print('em texto')
for i in "TEXTO":
    print(i)

arquivo = open('arquivo.txt')
soma = 0
# interest = 'Lorem'
interest = input('Digite a palavra que deseja contar: ')
total_interest = 0
for linha in arquivo:
    print('Caracteres na linha: ', len(linha))
    soma += len(linha)
    total_interest += linha.lower().count(interest.lower())
arquivo.close()

print('Arquivo com', soma, 'caracteres')
print('A palavra ', interest, 'apareceu ', total_interest)

   
# For para dicionário
#primeira maneira de ser feito
dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31,
    12: 30,
}

# qual_mes = int(input('Digite o número do mês (1..12): '))

# print('O mês', qual_mes, 'tem', dias_de_cada_mes[qual_mes], 'dias')

# print('Dias que faltam para acabar o ano, a partir do mês informado:')
# print(sum(list(dias_de_cada_mes.values())[qual_mes-1:])) # pega o dicionário e trabalha somente com os valores dentro das chaves
# # segunda maneira de ser feito, mas com o for range:
# total = 0
# for mes in range (qual_mes, 12 +1):
#     total += dias_de_cada_mes[mes]
# print ('modo estruturado')
# print('total de dias até o final do ano', total)

# For para dicionário:
for chave in dias_de_cada_mes:
    print('tenho uma chave nessa linha', chave)
    print('se eu tenho uma chave, tenho o valor', dias_de_cada_mes[chave])

for chave, valor in dias_de_cada_mes.items():
    print('Para a chave', chave, 'o valor', valor)

#tupla = ('Texto', 42, 5.01, int, str, list)
tupla = ('Text', 'texto de novo', 'textei', 'textando')
for isto in tupla:
    print(type(isto))
    print(isto)