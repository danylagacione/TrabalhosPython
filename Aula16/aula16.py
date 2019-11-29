# Aula 16 - 29-11-2019
# ?????????

#---sempre que possível usar o auto complete ctrl + espaço
# só se coloca o * para importar tudo o que está dentro do teu arquivo, 
#--------o ideal é chamar pelo nome da tua função.

from faixa import criar_faixa, salvar_faixa, ler_faixa 


#cadastro de playlist
#lendo musica, artista e album
musica = input('Digite uma musica:')
artista = input('Digite o nome de do artista:')
album = input('Digite o nome do album:')

faixa1 = criar_faixa(musica, album, artista) # variável que chama os dados do método não precisa ser o mesmo nome que está no método
salvar_faixa(faixa1)
lista = ler_faixa()

for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}')







