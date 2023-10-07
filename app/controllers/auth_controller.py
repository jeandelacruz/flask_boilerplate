from app import db
from app.models.users_model import UserModel


class AuthController:
    def __init__(self):
        self.db = db
        self.model = UserModel

    def sign_in(self, body):
        pass
