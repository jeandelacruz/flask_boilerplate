from app import api
from flask import request
from flask_restx import Resource
from http import HTTPStatus
from app.controllers.roles_controller import RoleController
from app.schemas.roles_schema import RoleRequestSchema

role_ns = api.namespace(
    name='Roles',
    description='Rutas del modulo Roles',
    path='/roles'
)

schema_request = RoleRequestSchema(role_ns)


# CRUD
@role_ns.route('')
class Roles(Resource):
    # dispatch
    def get(self):
        ''' Listar todos los roles '''
        controller = RoleController()
        return controller.fetch_all()

    @role_ns.expect(schema_request.create(), validate=True)
    def post(self):
        ''' Creación de un rol '''
        controller = RoleController()
        return controller.save(request.json)


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
