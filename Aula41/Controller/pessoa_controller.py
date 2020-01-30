from flask_restful import Resource


class PessoaController(Resource):
    def get(self):
        return 'Acesso a controladora pessoa pelo metodo HTTP GET'

    def post(self):
        return 'Acesso a controladora pessoa pelo metodo HTTP POST'

    def put(self):
        return 'Acesso a controladora pessoa  pelo metodo HTTP PUT'

    def delete(self):
        return 'Acesso a controladora pessoa  pelo metodo HTTP DELETE'