from app import db
from app.models.roles_models import RoleModel


class RoleController:
    def __init__(self):
        self.db = db
        self.model = RoleModel

    def all(self):
        return 'Listado de roles'
