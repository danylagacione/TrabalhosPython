import MySQLdb

class PessoaDao():
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskill.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA")
        pessoas = self.cursor.fetchall()
        return pessoas
    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA WHERE ID = {}".format(id))
        return 'Listando o dado de id: {}'.format(id)
    def insert(self, pessoa):
        return 'Cadastrando uma pessoa {}'.format(pessoa)
    def update(self, pessoa):
        return 'Alterando uma pessoa{}'.format(pessoa)
    def remove(self, id):
        return 'Removendo a pessoa de id: {}'.format(id)