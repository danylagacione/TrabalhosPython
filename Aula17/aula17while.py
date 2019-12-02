# Aula 17 02-12-2019
# Dicionários, While

# bole = True
# n=0

# while n <= 30:
#     n = n+1
#     print (f'Olá Turma{n}')

# while False:
#     n = n+1
#     print (f'Olá Turma{n}')

n = 0
# while n <= 30:
#     n = n+1
#     print (f'Olá Turma{n}')  
#     break
#     print ('Passou!')  

while n <= 30:
    n = n+1
    print (f'Olá Turma{n}') 
    if n == 10: 
        continue # o que estiver abaixo do continue não se executa, só faz sentido se estiver dentro de uma condição 
    print ('Passou!')  

    