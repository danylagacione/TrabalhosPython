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

    # def comprar (self, comprou_algo):
    #     if self.bens == True:
    #         self.bens = 'aumentou seus bens' 
    #     else:
    #         self.bens = 'Sim, diminuiu o dinheiro na carteira'     
        
    # def pagar_divida (self, dividas):
    #     if self.divida == True:
    #         if dividas :
    #             self.pagar_divida = 'Possui dívidas'
    #         else:
    #             self.pagar_divida = 'Não possui dívidas'    
        
                  
p = Cliente (70, '000.222.333-44', 'João', 20, 'M') 

p.receber_salario(800)
p.receber_salario (500)
# p.comprar(300) 
# p.pagar_divida (200)

print(f'Código do Cliente{p.codigo}, CPF: {p.cpf}, Nome:{p.nome}, Idade: {p.idade}, Sexo: {p.sexo}')
print(f'Recebeu o salário?{p.dinheiro_na_carteira}')
# print(f'Comprou algo?{p.bens}')
# print(f'Pagou a dívida?{p.pagar_divida}')


                             






