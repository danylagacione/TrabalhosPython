def criar_faixa(musica, album, artista):
    faixa = {'musica': musica, 'album': album, 'artista': artista} #armazenar o conjunto de dados do mesmo tipo no dicionario faz mais sentido
    return faixa

def salvar_faixa(faixa):
    arquivo = open('Aula16/faixas.txt', 'a') #o 'a' adiciona/abre/append o arquivo
#o arquivo.write é uma função
    arquivo.write(f"{faixa ['musica']};{faixa['album']};{faixa['artista']}\n")
    arquivo.close()    

def ler_faixa():
    arquivo = open('Aula16/faixas.txt', 'r')
    listas_faixas = [] #a lista tem que ser criada fora do FOR, pois se criada dentro ela vai ficar se subscrevendo.
    for linha in arquivo:
        linha = linha.strip()
        dados_faixa = linha.split(';')
        faixa = criar_faixa(dados_faixa[0], dados_faixa[1], dados_faixa[2])# ao invés de criar um novo dicionário, eu chamo o mesmo que está na 1ª função (reutilizo)
        listas_faixas.append(faixa)
    arquivo.close()
    return listas_faixas            

