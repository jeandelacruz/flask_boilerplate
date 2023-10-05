from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UserResponseSchema


class UserController:
    def __init__(self):
        self.db = db
        self.model = UserModel
        self.schema = UserResponseSchema

    def fetch_all(self):
        pass

    def save(self, body):
        pass

    def find_by_id(self, id):
        pass

    def update(self, id, body):
        pass

    def remove(self, id):
        pass
