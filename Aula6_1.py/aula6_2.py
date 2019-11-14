# Aula 6 - P2 - 12-11-2019
# Estruturas de repetição - FOR

<<<<<<< HEAD
#--- for simpes usando range com incremento padrão de 1
for i in range (0,10,):
    print (f'{i}- Padawans HbPy')
#--- for simpes usando range com incremento de 2
=======
#--- for simples usando range com incremento padrão de 1
for i in range (0,10,):
    print (f'{i}- Padawans HbPy')
#--- for simples usando range com incremento de 2
>>>>>>> 2d8463416993fc7b9ac4750ff272aa8e9b0ed328
for i in range (0,100,2):
    print (f' {i}- Pares')


#--- For em lista usando range
lista = ['Mateus', 'Matheus', 'Marcela', 'Nicole', 'Tonho', 'Pablo']
for i in range (0,6):
    print (lista[i])

#---Exemplificando o problema do uso de For em lista usando range
lista.append ('Natan')
for sortudo in lista:
    print (sortudo)

#---For usando os elementos da própria lista (foreach)
numero = 10
for i in range(0,10):
    print (f'{i} x {numero} = {i*numero}')

