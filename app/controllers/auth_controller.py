from os import getenv
from app import db, mail
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from http import HTTPStatus
from secrets import token_hex
from app.utils.mailing import Mailing


class AuthController:
    def __init__(self):
        self.db = db
        self.model = UserModel
        self.mailing = Mailing()

    def sign_in(self, body):
        try:
            username = body['username']
            # Operador Walrus
            # https://ellibrodepython.com/operador-walrus
            if record := self.model.where(username=username, status=True).first():
                # 2º Validar que la contraseña sea correcta
                password = body['password']
                if record.check_password(password):
                    # 3º Creación del JWT
                    user_id = record.id
                    access_token = create_access_token(identity=user_id)
                    refresh_token = create_refresh_token(identity=user_id)
                    return {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }, HTTPStatus.OK
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

    def refresh_token(self, identity):
        try:
            access_token = create_access_token(identity=identity)
            return {
                'access_token': access_token
            }, HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def password_reset(self, body):
        try:
            email = body['email']
            if record := self.model.where(email=email, status=True).first():
                return self._extracted_from_password_reset(record, email)
            return {
                'message': f'No se encontro un usuario con el correo: {email}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    # TODO Rename this here and in `password_reset`
    # Cuando se tiene un codigo largo es mejor separar la logica de las validaciones
    # ya que de esta manera podremos tener un codigo mas limpio
    def _extracted_from_password_reset(self, record, email):
        new_password = token_hex(6)
        record.password = new_password
        record.hash_password()

        self.db.session.add(record)
        self.db.session.commit()

        self.mailing.email_reset_password(
            email, record.name, new_password
        )

        return {
            'message': 'Se envio un correo con la nueva contraseña'
        }, HTTPStatus.OK
