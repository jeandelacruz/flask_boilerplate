from abc import ABC
# Incluimos las clases para poder agregarlo como su tipo en cada atributo
# https://cosasdedevs.com/posts/tipado-python/
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_mixins.smartquery import SmartQueryMixin
from marshmallow.schema import Schema
from http import HTTPStatus
from re import findall

# Definimos una clase abstracta, usamos el paquete ABC
# segun PIP 3119 https://peps.python.org/pep-3119/


class BaseController(ABC):
    def __init__(self):
        self.db: SQLAlchemy = None
        self.model: SmartQueryMixin = None
        self.schema: Schema = None
        self.messages: dict = None

    def _format_placeholders(self, message, data):
        # Si data es un diccionario, reemplaza los placeholders con los valores correspondientes del diccionario
        if isinstance(data, dict):
            placeholders = findall(r'\{(.*?)\}', message)
            for placeholder in placeholders:
                if placeholder in data:
                    message = message.replace(
                        f'{{{placeholder}}}', data[placeholder]
                    )
        # Si data no es un diccionario, asume que es el valor directo de reemplazo
        else:
            message = message.replace('{id}', str(data))

        return message

    def fetch_all(self):
        records = self.model.where(status=True).all()
        response = self.schema(many=True)
        return response.dump(records)

    def save(self, body):
        try:
            record_new = self.model.create(**body, commit=False)

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

    def find_by_id(self, id):
        try:
            if record := self.model.where(id=id, status=True).first():
                response = self.schema(many=False)
                return response.dump(record), HTTPStatus.OK

            return {
                'message': self._format_placeholders(
                    self.messages['not_found'], id
                )
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def update(self, id, body):
        try:
            if record := self.model.where(id=id, status=True).first():
                record.update(**body)
                message = self._format_placeholders(
                    self.messages['update'], id
                )
                return self._extracted_from_transactional(record, message)
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

    def remove(self, id):
        try:
            if record := self.model.where(id=id, status=True).first():
                record.update(status=False)
                message = self._format_placeholders(
                    self.messages['remove'], id
                )
                return self._extracted_from_transactional(record, message)
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

    # TODO Rename this here and in `update` and `remove`
    def _extracted_from_transactional(self, record, message):
        self.db.session.add(record)
        self.db.session.commit()
        return {'message': message}, HTTPStatus.OK
