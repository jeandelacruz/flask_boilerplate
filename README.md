# Boilerplate Flask

---

## Modelos:

- Usuarios

  | campo     | tipo         | constraint           |
  | --------- | ------------ | -------------------- |
  | id        | SERIAL       | PRIMARY KEY          |
  | name      | VARCHAR(120) | NOT NULL             |
  | last_name | VARCHAR(150) | NOT NULL             |
  | username  | VARCHAR(80)  | UNIQUE               |
  | password  | VARCHAR(255) | NOT NULL             |
  | email     | VARCHAR(160) | UNIQUE               |
  | rol_id    | INT          | FOREIGN KEY NOT NULL |
  | status    | BOOLEAN      | -                    |

- Roles

  | campo  | tipo    | constraint  |
  | ------ | ------- | ----------- |
  | id     | SERIAL  | PRIMARY KEY |
  | name   | CHAR(8) | NOT NULL    |
  | status | BOOLEAN | -           |

## Caracteristicas:

1. Login
   - [x] Creación del token de acceso (JWT | access_token - refresh_token)
   - [x] Validación de contraseñas encriptadas (bcrypt)
2. Registro
   - [x] Encriptación de contraseña (bcrypt)
3. Recuperar Contraseña
   - [x] Generar una nueva contraseña encriptada
   - [x] Enviar un correo con un template (html)
4. CRUD por cada Modelo
   - [x] Listado con paginación
   - [x] Obtener un registro mediante el id
   - [x] Creación de un registro
   - [x] Actualización de un registro
   - [x] Eliminar un registro (SoftDelete)
5. Decoradores
   - [x] Proteger las rutas mediante autenticación
   - [x] Proteger las rutas por rol
6. Documentación y validaciones
   - [x] Swagger OpenAPI
   - [x] Schemas
7. Despliegue
   - [x] Render

## PIP

```ssh
pip install Flask Flask-Migrate flask-restx Flask-SQLAlchemy psycopg2-binary python-dotenv sqlalchemy-mixins autopep8 marshmallow-sqlalchemy bcrypt flask-jwt-extended Flask-Mail
```

## Enviroments

```py
FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_DEBUG=True
FLASK_ENV=development

DATABASE_URL='postgresql://user:password@localhost:5432/name_database'

SECRET_KEY=''

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME='@gmail.com'
MAIL_PASSWORD=''
```

## Documentación

- SQLAlchemy
  - [Metodos usados con el Modelo](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.all)
  - [Tipo de datos](https://docs.sqlalchemy.org/en/14/core/types.html)
  - [Metodos optimos (adicionales)](https://github.com/absent1706/sqlalchemy-mixins/blob/master/README.md)
- FlaskRestX
  - [Tipo de datos en validación](https://flask-restx.readthedocs.io/en/latest/_modules/flask_restx/fields.html)
  - [Response](https://flask-restx.readthedocs.io/en/latest/marshalling.html)
  - [Request Parser](https://flask-restx.readthedocs.io/en/latest/parsing.html)
  - [Swagger](https://flask-restx.readthedocs.io/en/latest/swagger.html)
- FlaskJWTExtended
  - [Protección de rutas](https://flask-jwt-extended.readthedocs.io/en/stable/optional_endpoints.html)
- Operador Walrus
  - [Documentación](https://ellibrodepython.com/operador-walrus)

## Comandos

### Migraciones

- Iniciar el paquete alembic (Una sola vez, siempre y cuando no exista la carpeta **migrations**)

```ssh
flask db init
```

- Crear una migración (Crea o se modifica un modelo, explicitamente en los campos)

```ssh
flask db migrate -m "comentario"
```

- Sincronizar las migraciones

```ssh
flask db upgrade
```
