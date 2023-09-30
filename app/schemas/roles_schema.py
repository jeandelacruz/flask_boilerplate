from flask_restx import fields


class RoleRequestSchema:
    def __init__(self, namespace):
        self.ns = namespace

    def create(self):
        return self.ns.model('Role Create', {
            'name': fields.String(required=True, max_length=8)
        })
