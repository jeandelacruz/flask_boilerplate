from app import api
from flask_restx import Resource
from http import HTTPStatus
from app.controllers.roles_controller import RoleController

role_ns = api.namespace(
    name='Roles',
    description='Rutas del modulo Roles',
    path='/roles'
)


# CRUD
@role_ns.route('')
class Roles(Resource):
    # dispatch
    def get(self):
        ''' Listar todos los roles '''
        controller = RoleController()
        return controller.all()

    def post(self):
        ''' Creación de un rol '''
        return 'Creación de rol', HTTPStatus.CREATED


@role_ns.route('/<int:id>')
class RoleById(Resource):
    def get(self, id):
        ''' Obtener un rol por su id '''
        return f'Obtener {str(id)}', HTTPStatus.OK

    def put(self, id):
        ''' Actualizar un rol por su id, enviando el objeto completo '''
        return f'Actualizar {str(id)}'

    def patch(self, id):
        ''' Actualizar un rol por su id, enviando el objeto parcial '''
        return f'Actualizar {str(id)}'

    def delete(self, id):
        ''' Inhabilitar un rol por su id '''
        return f'Eliminar {str(id)}', HTTPStatus.OK
