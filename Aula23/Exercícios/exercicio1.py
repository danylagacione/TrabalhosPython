# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

#dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto em uma variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

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
        self.codigo = int(cliente [0])
        self.nome = cliente[1]
        self.idade = int(cliente[2])
        self.sexo = cliente[3]
        self.email = cliente[4]
        self.telefone = int(cliente[5])


c = Cliente(dadobruto)
c.tratar_dadobruto()

print (f' Código do Cliente: {c.codigo}')
print (f'nome do cliente: {c.nome}')
print (f'idade do cliente: {c.idade}')
print (f'sexo do cliente: {c.sexo}')
print (f'E-mail do cliente: {c.email}')
print(f'Telefone do cliente: {c.telefone}')

######### usando o def __str__ retorna os dados em texto 

def __str__(self):
    texto = f'''
    codigo: {self.codigo}
    nome: {self.nome}
    idade: {self.idade}
    sexo: {self.sexo}
    email: {self.email}
    telefone: {self.telefone} '''
    return texto



        
        


        


