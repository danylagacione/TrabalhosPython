class Endereco:
    id = 0
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    cep = ''

    def exportar_txt(self, lista_enderecos):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('Aula33/Aula33-4/enderecos4.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for e in lista_enderecos:
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'