from app import api
from flask import request
from flask_restx import Resource
from app.schemas.auth_schema import AuthRequestSchema
from app.controllers.auth_controller import AuthController

auth_ns = api.namespace(
    name='Authentication',
    description='Rutas del modulo Authentication',
    path='/auth'
)

schema_request = AuthRequestSchema(auth_ns)


@auth_ns.route('/signin')
class SignIn(Resource):
    @auth_ns.expect(schema_request.login(), validate=True)
    def post(self):
        ''' Login de usuario '''
        controller = AuthController()
        return controller.sign_in(request.json)
