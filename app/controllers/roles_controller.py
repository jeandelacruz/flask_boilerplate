from app import db
from app.models.roles_model import RoleModel
from app.schemas.roles_schema import RoleResponseSchema
from app.controllers import BaseController


class RoleController(BaseController):
    def __init__(self):
        self.db = db
        self.model = RoleModel
        self.schema = RoleResponseSchema
        self.messages = {
            'save': 'El rol {name} se creo con exito',
            'not_found': 'No se encontro un rol con el ID: {id}',
            'update': 'El rol con el ID: {id} ha sido actualizado',
            'remove': 'El rol con el ID: {id} ha sido inhabilitado'
        }
