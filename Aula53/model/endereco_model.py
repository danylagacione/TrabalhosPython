
#--- Importação da classe principal do alchemy
import sqlalchemy as db
#--- Importação do metodo para gerar a classe base do Alchemy que fará o mapeamento da tabela do banco de dados
from sqlalchemy.ext.declarative import declarative_base
#--- Geração da classe que sera usado na herança para mapear a tabela do banco de dados
BaseAlchemy = declarative_base()
#--- Criação da classe para model produto usando herança da classe base do alchemy criada na linha anterior
class EnderecoModel(BaseAlchemy):
    # --- variável que define qual tabela será usada para mapear a classe
    __tablename__ = "endereco"
    # --- Declaração de variáveis que serão mapeadas de acordo com as colunas da tabela no banco de dados
    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(length=45))
    numero = db.Column(db.String(length=50))
    complemento = db.Column(db.String(length=45))
    bairro = db.Column(db.String(length=45))
    cidade = db.Column(db.String(length=45))
    cep = db.Column(db.String(length=45))

    # --- Sobreescrita do método para conversão do objeto da classe em uma string para imprimir as variáveis
    def __str__(self):
        return f"{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}"
