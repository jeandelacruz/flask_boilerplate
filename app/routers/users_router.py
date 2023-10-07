from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.users_schema import UserRequestSchema
from app.controllers.users_controller import UserController


user_ns = api.namespace(
    name='Users',
    description='Rutas del modulo Users',
    path='/users'
)

schema_request = UserRequestSchema(user_ns)


@user_ns.route('')
@user_ns.doc(security='Bearer')
class Users(Resource):
    @jwt_required()
    @user_ns.expect(schema_request.all())
    def get(self):
        ''' Listar todos los usuarios '''
        query_params = schema_request.all().parse_args()
        controller = UserController()
        return controller.fetch_all(query_params)

    @jwt_required()
    @user_ns.expect(schema_request.create(), validate=True)
    def post(self):
        ''' Creación de un usuario '''
        controller = UserController()
        return controller.save(request.json)


@user_ns.route('/<int:id>')
@user_ns.doc(security='Bearer')
class UserById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un usuario por su id '''
        controller = UserController()
        return controller.find_by_id(id)

    @jwt_required()
    @user_ns.expect(schema_request.update(), validate=True)
    def patch(self, id):
        ''' Actualizar un usuario por su id, enviando el objeto parcial '''
        controller = UserController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Inhabilitar un usuario por su id '''
        controller = UserController()
        return controller.remove(id)
