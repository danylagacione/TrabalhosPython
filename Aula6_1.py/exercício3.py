#--- Exercício 1 - Foreach
#--- Escreva um programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- o nome dos alunos
#           2-Média do aluno
#           3-Resultado (Aprovaado>=7.0)

nomes = []
notas = []
media = 0
a = 0
b = 1
c = 2
d = 3

for i in range (0,10):
    nomes.append (input (f'nome aluno {i+1}'))
    for j in range (0,4):
        notas.append (float(input (f'nota aluno {j+1}')))

for alunos in nomes:
    media = (notas[a] + notas[b] + notas[c] + notas[d])/4
    print(f'nome: {alunos}')
    print(f'\nnome: {alunos}')
    print(f'media: {media}')
    if media >= 7:
        print('Aprovado!')
    else: 
        print ('reprovado')
    a = a+4
    b = b+4
    c = c+4
    d=  d+4