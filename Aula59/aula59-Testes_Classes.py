
# Teste 2 - Classe

# class Calc:
#     def __init__(self):
#         # variável de classe
#         self.__n1 = 0
#         self.__n2 = 0
#         self.__resultado = 0
#
# c = Calc ()
# assert isinstance(c, Calc)

# Testar todos os métodos da classe
class Calc:
    def __init__(self, numero1, numero2):
        # variável de classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
        return valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
        return valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        self.__resultado = self.__n1 + self.__n2
        return self.__resultado

    def subtracao(self):
        self.__resultado = self.__n1 - self.__n2
        return self.__resultado

    def multiplicacao(self):
        self.__resultado = self.__n1 * self.__n2
        return self.__resultado

c = Calc(10,20)
assert isinstance(c, Calc)
assert c.soma() == 30
assert c.soma() != 20
assert c.soma() > 10
assert c.soma() == c.get_resultado()

assert c.subtracao() == -10
assert c.subtracao() != 20
assert c.subtracao() > -20
assert c.subtracao() == c.get_resultado()

assert c.set_n1(5) == c.get_n1()
assert c.set_n2(8) == c.get_n2()




