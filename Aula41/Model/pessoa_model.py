
class PessoaModel:
    def __init__(self, nome, sobrenome, idade, id=None): # o parametro que for ficar opcional tem sempre que ser o último
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade