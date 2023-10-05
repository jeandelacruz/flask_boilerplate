from app import api
from flask_restx import Resource
from flask import request
from app.schemas.users_schema import UserRequestSchema
from app.controllers.users_controller import UserController


user_ns = api.namespace(
    name='Users',
    description='Rutas del modulo Users',
    path='/users'
)

schema_request = UserRequestSchema(user_ns)


@user_ns.route('')
class Users(Resource):
    def get(self):
        ''' Listar todos los usuarios '''
        controller = UserController()
        return controller.fetch_all()

    @user_ns.expect(schema_request.create(), validate=True)
    def post(self):
        ''' Creación de un usuario '''
        controller = UserController()
        return controller.save(request.json)


@user_ns.route('/<int:id>')
class UserById(Resource):
    def get(self, id):
        ''' Obtener un usuario por su id '''
        controller = UserController()
        return controller.find_by_id(id)

    @user_ns.expect(schema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un usuario por su id, enviando el objeto parcial '''
        controller = UserController()
        return controller.update(id, request.json)

    def delete(self, id):
        ''' Inhabilitar un usuario por su id '''
        controller = UserController()
        return controller.remove(id)
