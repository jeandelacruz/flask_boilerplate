from app import jwt
from app.models import users_model as model


# Es un decorador proporcionado por Flask-JWT-Extended que registra una
# función callback para buscar y cargar un usuario basado en el contenido del token JWT.
@jwt.user_lookup_loader
# Esta función toma dos argumentos: header y data. header contiene
# el encabezado del token JWT y data contiene el contenido (payload) del token
def user_lookup_callback(header, data):
    user = model.UserModel
    # El campo 'sub' (que significa "subject") en el payload del
    # JWT suele contener el identificador único del usuario, como un ID de usuario.
    identity = data['sub']
    return user.where(id=identity).first()


# Es un decorador proporcionado por Flask-JWT-Extended que registra una
# función callback para determinar la identidad del usuario cuando se crea un token JWT.
@jwt.user_identity_loader
# Esta función toma un único argumento, user, que es el usuario para el cual se está creando el token.
def user_identity_lookup(user):
    # Esta línea simplemente devuelve el usuario si existe o None si no. No obstante, esta línea parece un
    # poco redundante, ya que podría simplemente devolver el user directamente.
    return user or None
