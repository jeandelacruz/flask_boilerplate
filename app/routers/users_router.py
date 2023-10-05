from app import api
from flask_restx import Resource


user_ns = api.namespace(
    name='Users',
    description='Rutas del modulo Users',
    path='/users'
)


@user_ns.route('')
class Users(Resource):
    def get(self):
        ''' Listar todos los usuarios '''
        pass

    def post(self):
        ''' Creación de un usuario '''
        pass


@user_ns.route('/<int:id>')
class UserById(Resource):
    def get(self, id):
        ''' Obtener un usuario por su id '''
        pass

    def patch(self, id):
        ''' Actualizar un usuario por su id, enviando el objeto parcial '''
        pass

    def delete(self, id):
        ''' Inhabilitar un usuario por su id '''
        pass
