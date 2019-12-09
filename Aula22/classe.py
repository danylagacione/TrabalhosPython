#--- Aula 22 - 09-12-2019

# # 1) O que uma pessoa Tem? Quais as caracteristicas? 
# ######## Atributos ----- que podem ser convertidos em variáveis
# nome
# idade
# telefone
# sexo

# # 2) O que uma pessoa faz?
# ###### Métodos (funções/procedimento)  podem ter um return ou apenas um print 
# respira
# dorme
# correr 
# bebe
# come
# reproduz

# # 3) Como a pessoa está agora? 
# # Atributos de estado - variáveis (os dados das variáveis devem ser válidos/consistentes, fazer sentido)
# dividas
# cansada
# viva
# fome
# sede

#### FAZENDO UMA CLASSE
# O ideal do nome de uma classe é sempre a primeira letra estar em CapsLock ex: PessoaViva
# parametos da classe (self, nome1, idade1, telefone1, sexo1)
class Pessoa:
    '''
    Esta casse é uma demonstração para aula
    '''
    def __init__(self, nome1, idade1, telefone1, sexo1): 
        '''
        O __int__ é o motor que irá iniciar as variáveis da classe
        o self é o que irá conectar toda a classe
        '''
        #--- ATRIBUTOS -----
        self.nome = nome1 # a variável self.nome recebe o parametro nome1
        self.idade = idade1
        self.telefone1 = telefone1
        self.sexo = sexo1
        # ---- ATRIBUTOS DE ESTADO ----
        self.dividas = None
        self.cansada = 'não'
        self.viva = True 
        self.fome = 'n'
        self.sede = 'não'

    #### MÉTODOS
    def respira (self, respira):
        if self.viva == True:
            if respirar == True:
                self.viva = True
            else:
                self.viva = False    
    
    def corre (self, distancia):
        if self.viva:
            if distancia < 100:
                self.cansada = 'pouco'
                self.sede = 'pouco'
                self.fome = 'pouco'
            elif distancia >= 100 and distancia < 200:
                self.cansada = 'medio'
                self.sede = 'medio'
                self.fome = 'medio' 
            elif distancia >= 200:
                self.cansada = 'muito'
                self.sede = 'muito'
                self.fome = 'muito'       
        

    def dorme (self):
        if self.viva:
            self.cansada = 'não'
            self.bebe()
            self.fome()    

    def bebe (self):
        if self.viva:
            self.sede = 'não'

    def come (self):
        if self.viva:
            self.fome = 'não'

    def reproduz (self):
        pass # para outra hora

p = Pessoa('Antonio', 18, '47991999985', 'm')

# p.respira(False)

# p.respira (True)

p.corre(300)
p.dorme()
# p.fome()
# p.bebe()

print (f' Nome é {p.nome}') # colocando p.e o nome da variável, acessa a informação dela
print (f'Está vivo? {p.viva}')
print (f'Está com fome? {p.fome}')
print (f'Está com sede? {p.sede}')
print (f'Está cansada? {p.cansada}')

