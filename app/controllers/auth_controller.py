from app import db
from app.models.users_model import UserModel
from http import HTTPStatus


class AuthController:
    def __init__(self):
        self.db = db
        self.model = UserModel

    def sign_in(self, body):
        try:
            username = body['username']
            # 1º Validar que exista el usuario y este activo
            record = self.model.where(username=username, status=True).first()
            if record:
                # 2º Validar que la contraseña sea correcta
                password = body['password']
                if record.check_password(password):
                    return {}
                return {
                    'message': 'La contraseña es incorrecta'
                }, HTTPStatus.UNAUTHORIZED

            return {
                'message': f'No se encontro el usuario: {username}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
