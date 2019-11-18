#--- Exercício 1 -Dicionário
#--- Escreva um programa que leia os dados de cerveja
#--- Cerveja: Marca, Tipo, IBU, ABV, EBC, volume
#--- Crie um dicionário para armazenar os dados
#--- Imprima os dados do dicionário (não dicionário completo)


#cerveja = {}
marca = input('informar a marca')
tipo = input ('informar o tipo')
ibu = int (input ('informar o IBU'))
abv = input ('informar o ABV')
ebc = input ('informar o EBC')
volume = int (input ('informar o volume'))

informacoes = {'marca': marca,'tipo':tipo,'IBU': ibu,'ABV':abv,'EBC': ebc,'volume': volume }
print(f"{informacoes ['marca']} { informacoes ['tipo']} {informacoes ['IBU']} { informacoes ['ABV']} {informacoes['EBC']} {informacoes['volume']} ") 


#--- Correção 2/ exemplo 2 ---#
#--- Resolvido por Gustavo Antunes Voltolini
cerveja = {}
cerveja ['Marca'] = (input('Digite a marca: '))
cerveja ['Tipo'] = (input('Digite o tipo: '))
cerveja ['IBU'] = int(input('Digite o IBU(inteiros): '))
cerveja ['ABV'] = float(input('Digite o ABV(inteiros): '))
cerveja ['EBC'] = float(input('Digite o EBC: '))
cerveja ['volume'] = float(input('Digite o volume: '))

print (f"Marca{cerveja['Marca']} - Tipo: {cerveja['Tipo']} - IBU: {cerveja['IBU']} - ABV: {cerveja['ABV']} - EBC: {cerveja['EBC']} - Volume: {cerveja['volume']}")
