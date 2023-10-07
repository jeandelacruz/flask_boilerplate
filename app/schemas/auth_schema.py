from flask_restx import fields


class AuthRequestSchema:
    def __init__(self, namespace):
        self.ns = namespace

    def login(self):
        return self.ns.model('Auth SignIn', {
            'username': fields.String(required=True, max_length=80),
            'password': fields.String(required=True, max_length=18)
        })
