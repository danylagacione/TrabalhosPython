
#--- Criação da classe base de acessoa ao banco de dados
import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker

# class BaseDao:
#     def __init__(self):
#         # ----database+conector://user:passwd@url:porta/database
#         conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
#         criador_sessao = db.orm.sessionmaker()
#         criador_sessao.configure(bind=conexao)
#         self.sessao = criador_sessao()

#--- Criação da classe base de acessoa ao banco de dados
class BaseDao:
    # --- declaração do método construtor para definir as configurações de acesso ao banco de dados
    def __init__(self):
        # --- Declaração da engine de acesso passando as informações para conectar ao banco de dados
        # ----database+conector://user:passwd@url:porta/database
        conexao = db.create_engine("mysql+mysqlconnector://root@127.0.0.1:3306/aulabd")
        # --- Declaração da variável para geração de uma sessao com o banco de dados
        criador_sessao = db.orm.sessionmaker()
        # --- Configuração para que a sessão ao ser gerada, utilize os dados de acesso ao banco criados nas linhas anteriores
        criador_sessao.configure(bind=conexao) # usa a cariável bind para fazer a conexão com a url do banco de dados
        # --- Criação de uma sessao com o banco de dados
        self.sessao = criador_sessao()

    def listar_todos(self) -> list:
        return self.sessao.query(self.model_type).all()

    def buscar_por_id(self, id):
        return self.sessao.query(self.model_type).filter_by(id=id).one()

    def deletar(self, id) -> str:
        model = self.sessao.query(self.model_type).filter_by(id=id).one()
        self.sessao.delete(model)
        self.sessao.commit()
        return f"Deletado obj de id {id}"

    def inserir(self, model) -> str:
        self.sessao.add(model)
        self.sessao.commit()
        return f"Obj de id: {model.id} criada"

    def alterar(self, model) -> str:
        self.sessao.merge(model)
        self.sessao.commit()
        return f"Obj {model.nome} alterado com sucesso!"