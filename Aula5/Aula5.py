# Crie um programa que leia 4 notas
# Imprima a maior nota
# Imprima a menor nota
# Imprima a média
# Imprima se o aluno foi aprovado ou reprovado (Media 7.0)

nota1 = int (input ('digite a nota1'))
nota2 = int (input ('digite a nota2'))
nota3 = int (input ('digite a nota3'))
nota4 = int (input ('digite a nota4'))

if nota1 >= nota2 and nota1 >= nota3 and nota1 >= nota4: 
    print(f'a nota {nota1} é maior')
elif nota2 >= nota1 and nota2 >= nota3 and nota2 >= nota4:
    print (f'a nota {nota2} é a maior')
elif nota3 >= nota1 and nota3 >= nota2 and nota3 >= nota4:
    print (f' a nota {nota3} é maior')
else:
    print(f' a nota {nota4} é maior')  


if nota1 <= nota2 and nota1 <= nota3 and nota1 <= nota4: 
    print(f'a nota {nota1} é menor')
elif nota2 <= nota1 and nota2 <= nota3 and nota2 <= nota4:
    print (f'a nota {nota2} é a menor')
elif nota3 <= nota1 and nota3 <= nota2 and nota3 <= nota4:
    print (f' a nota {nota3} é menor')
else:
    print(f' a nota {nota4} é menor') 

media = (nota1 + nota2 + nota3 + nota4) / 4
 

print (f'media das notas: {media}')

if media >= 7:
    print (f'o aluno foi aprovado {media}')
else:
     print (f' o aluno foi reprovado {media}')







