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
   - [] Creación del token de acceso (JWT | access_token - refresh_token)
   - [] Validación de contraseñas encriptadas (bcrypt)
2. Registro
   - [] Encriptación de contraseña (bcrypt)
3. Recuperar Contraseña
   - [] Generar una nueva contraseña encriptada
   - [] Enviar un correo con un template (html)
4. CRUD por cada Modelo
   - [] Listado con paginación
   - [] Obtener un registro mediante el id
   - [] Creación de un registro
   - [] Actualización de un registro
   - [] Eliminar un registro (SoftDelete)
5. Decoradores
   - [] Proteger las rutas mediante autenticación
   - [] Proteger las rutas por rol
6. Documentación y validaciones
   - [] Swagger OpenAPI
   - [] Schemas
7. Despliegue
   - [] Render

## PIP

```ssh
pip install Flask Flask-Migrate flask-restx Flask-SQLAlchemy psycopg2-binary python-dotenv sqlalchemy-mixins
```

## Enviroments

```json
FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_DEBUG=True
FLASK_ENV=development

DATABASE_URL='postgresql://user:password@localhost:5432/name_database'
```

## Documentación

- FlaskRestX
  - [Swagger](https://flask-restx.readthedocs.io/en/latest/swagger.html)

## Comandos
