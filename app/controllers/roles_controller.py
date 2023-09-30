from app import db
from app.models.roles_models import RoleModel
from http import HTTPStatus


class RoleController:
    def __init__(self):
        self.db = db
        self.model = RoleModel

    def fetch_all(self):
        # SELECT * FROM roles;
        records = self.model.all()
        print(records)
        return []

    def save(self, body):
        try:
            record_new = self.model.create(**body)
            self.db.session.add(record_new)
            self.db.session.commit()
            return {
                'message': f'El rol {body["name"]} se creo con exito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()
