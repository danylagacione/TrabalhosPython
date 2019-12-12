# Aula 22 -  09-12-2019

#---- Crie uma classe Cliente
# 1) deve ter como atributos: código, CPF, nome, idade, sexo

# 2) como métodos: receber salário, comprar, pagar divida
# Quando recebe aumenta dinheiro na carteira.
# Quando compra aumenta os bens e diminui o dinheiro na carteira
# Se comprar e não tiver dinheiro suficiente deve diminuir o dinheiro da carteira e aumentar a divida
# Para pagar a divida tem que ter dinheiro suficiente na carteira

# 3) Atributos de estado: dinheiro na carteira, divida, bens

class Cliente:
    def __init__(self, codigo1, cpf1, nome1, idade1, sexo1):
        self.codigo = codigo1
        self.cpf = cpf1
        self.nome = nome1
        self.idade = idade1
        self.sexo = sexo1
        # Atributos de estado
        self.dinheiro_na_carteira = 0
        self.divida = 0
        self.bens = 0

    def receber_salario (self, salario):
        if self.dinheiro_na_carteira == 0:
            self.dinheiro_na_carteira = salario
        else:
            self.dinheiro_na_carteira = self.dinheiro_na_carteira + salario

    def comprar (self, tem_bens):
        if self.bens == 0:
            self.bens = tem_bens
            if self.bens >= 1:
                self.bens = self.bens - self.dinheiro_na_carteira 
            else:
                self.bens = self.bens + self.dinheiro_na_carteira 
                      
    def pagar_divida (self, dividas):
        if self.divida == 0:
            self.divida = dividas
            if dividas :
                self.pagar_divida = self.pagar_divida - self.dinheiro_na_carteira
            else:
                self.pagar_divida
        
                  
p = Cliente (70, '000.222.333-44', 'João', 20, 'M') 

p.receber_salario(800)
#p.receber_salario (500)
p.comprar(300) 
p.pagar_divida (0)

print(f'Código do Cliente{p.codigo}, CPF: {p.cpf}, Nome:{p.nome}, Idade: {p.idade}, Sexo: {p.sexo}')
print(f'Recebeu o salário?{p.dinheiro_na_carteira}')
print(f'Comprou algo?{p.bens} esse é o valor que tens na carteira após comprar algo')
print(f'Pagou a dívida?{p.pagar_divida}')


                             






