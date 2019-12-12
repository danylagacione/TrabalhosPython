# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

#dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não esteja desatualizado.

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'
class Cliente:
    def __init__(self, dadobruto):
        self.dado_bruto = dadobruto
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

        
    def tratar_dadobruto (self):
        cliente = self.dado_bruto.strip().split(';')
        self.codigo = int(cliente[0])
        self.nome = cliente[1]
        self.idade = int(cliente[2])
        self.sexo = cliente[3]
        self.email = cliente[4]
        self.telefone = cliente[5]

    def salvar_arquivo (self):
        arquivo = open ('Aula23/Exercícios/dadosclientes.txt', 'a')
        arquivo.write(f'{self.codigo}; {self.nome}; {self.idade}; {self.sexo}; {self.email};{self.telefone}\n') 
        arquivo.close()

    def atualizar_dados (self):
        self.nome = input('Digite a alteração do nome do ciente:')
        self.idade = int(input('Digite a alteração da idade do cliente:'))
        self.sexo = (input('Digite a alteração do sexo do cliente:'))
        self.email = (input('Digite a alteração do e-mail do cliente:'))
        self.telefone = (input('Digite a alteração do telefone cliente:'))
        self.dado_bruto = (f'{self.codigo}; {self.nome}; {self.idade}; {self.sexo}; {self.email};{self.telefone}\n') 


                        

c = Cliente(dadobruto)
c.tratar_dadobruto()
c.salvar_arquivo()
c.atualizar_dados()

print (f' Código do Cliente: {c.codigo}')
print (f'nome do cliente: {c.nome}')
print (f'idade do cliente: {c.idade}')
print (f'sexo do cliente: {c.sexo}')
print (f'E-mail do cliente: {c.email}')
print(f'Telefone do cliente: {c.telefone}')

