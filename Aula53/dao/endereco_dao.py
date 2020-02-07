

from Aula53.dao.base_dao import BaseDao
from Aula53.model.endereco_model import EnderecoModel

#--- Criação da classe para realizar as operações na tabela produto
#--- Criado classe utilizando herança da classe BaseDao, que possui as configurações de acesso a base
class EnderecoDao(BaseDao):
    # --- Declaração do método de listagem de todos os dados da tabela utilizando a sessao com o banco de dados criada na classe 'Mâe'
    def list_all(self):
        return self.sessao.query(EnderecoModel).all() # retorna todos os dados da tabela convertidos para essa classe
    def list_by_id(self,id):
        return self.sessao.query(EnderecoModel).filter_by(id=id).one() # o filter_by pega as colunas que foram pré definidas
    def delete(self,id):
        objeto_model = self.sessao.query(EnderecoModel).filter_by(id=id)
        self.sessao.delete(objeto_model)
        self.sessao.coommit() # sempre dar o commit para a informação ser enviada para o banco de dados
        return f'Deletado objeto de id {id}'