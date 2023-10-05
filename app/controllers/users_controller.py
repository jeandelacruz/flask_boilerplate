from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UserResponseSchema
from http import HTTPStatus


class UserController:
    def __init__(self):
        self.db = db
        self.model = UserModel
        self.schema = UserResponseSchema

    def fetch_all(self):
        pass

    def save(self, body):
        try:
            record_new = self.model.create(**body)
            record_new.hash_password()
            self.db.session.add(record_new)
            self.db.session.commit()

            return {
                'message': f'El usuario {body["username"]} se creo con exito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def find_by_id(self, id):
        pass

    def update(self, id, body):
        pass

    def remove(self, id):
        pass
