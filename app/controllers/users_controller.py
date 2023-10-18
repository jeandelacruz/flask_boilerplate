from app import db
from app.controllers import BaseController
from app.models.users_model import UserModel
from app.schemas.users_schema import UserResponseSchema
from sqlalchemy import or_
from http import HTTPStatus


class UserController(BaseController):
    def __init__(self):
        self.db = db
        self.model = UserModel
        self.schema = UserResponseSchema
        self.messages = {
            'save': 'El usuario {username} se creo con exito',
            'not_found': 'No se encontro un usuario con el ID: {id}',
            'update': 'El usuario con el ID: {id} ha sido actualizado',
            'remove': 'El usuario con el ID: {id} ha sido inhabilitado'
        }

    def fetch_all(self, query_params):
        # Paginación
        # Pagina (a obtener)
        # Nº Registros x pagina
        # Total 100 usuarios
        # Pagina 1
        # SELECT * FROM users LIMIT 10 OFFSET 0 --(nº pagina - 1) * nº registros x pagina
        # Pagina 2
        # SELECT * FROM users LIMIT 10 OFFSET 100
        try:
            filters = {}
            page = query_params['page']
            per_page = query_params['per_page']
            if query := query_params.get('q', None):
                filters = {
                    or_: {
                        'username__ilike': f"%{query}%",
                        'name__ilike': f"%{query}%",
                        'last_name__ilike': f"%{query}%"
                    }
                }

            # Aqui vamos a realizar multiples filtros
            # https://github.com/absent1706/sqlalchemy-mixins#all-in-one-smart_query
            records = self.model.smart_query(
                filters={**filters},
            ).paginate(
                page=page,
                per_page=per_page
            )

            response = self.schema(many=True)

            return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }, HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def save(self, body):
        try:
            record_new = self.model.create(**body)
            record_new.hash_password()
            self.db.session.add(record_new)
            self.db.session.commit()

            return {
                'message': self._format_placeholders(
                    self.messages['save'], body
                )
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def update(self, id, body):
        try:
            if record := self.model.where(id=id, status=True).first():
                record.update(**body)
                self.db.session.add(record)
                self.db.session.commit()

                message = self._format_placeholders(
                    self.messages['update'], id
                )
                return self._extracted_from_transactional(
                    record, message
                )
            return {
                'message': self._format_placeholders(
                    self.messages['not_found'], id
                )
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
        finally:
            self.db.session.close()

    def profile_me(self, identity):
        try:
            record = self.model.where(id=identity).first()
            response = self.schema(many=False)
            return response.dump(record), HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
