from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.users_model import UserModel


class UserRequestSchema:
    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model('User Create', {
            'name': fields.String(required=True, max_length=120),
            'last_name': fields.String(required=True, max_length=150),
            'username': fields.String(required=True, max_length=80),
            'password': fields.String(required=True, max_length=255),
            'email': fields.String(required=True, max_length=160),
            'rol_id': fields.Integer(required=True)
        })

    def update(self):
        return self.ns.model('User Update', {
            'name': fields.String(required=False, max_length=120),
            'last_name': fields.String(required=False, max_length=150),
            'username': fields.String(required=False, max_length=80),
            'password': fields.String(required=False, max_length=255),
            'email': fields.String(required=False, max_length=160),
            'rol_id': fields.Integer(required=False)
        })


class UserResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
