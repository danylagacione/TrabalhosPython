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

