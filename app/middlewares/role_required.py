# Es un decorador que ayuda a preservar la metainformación de la función original cuando esta es decorada.
from functools import wraps
# Representa al usuario actualmente autenticado, esto lo hacemos gracias a la inyeccion de utils/jwt.py
from flask_jwt_extended import current_user
from http import HTTPStatus


def role_required(rol_id):
    # Esta es la función de envoltorio que acepta la función fn que será eventualmente decorada.
    def wrapper(fn):
        # Aquí se define el decorador real que envolverá la función fn.
        # El decorador @wraps(fn) asegura que la metainformación de fn (como su nombre, docstring, etc.)
        # se mantenga intacta después de ser decorada.
        @wraps(fn)
        def decorator(*args, **kwargs):
            # Logica del decorador
            # Obtenemos el rol_id del usuario conectado
            role_user = current_user.rol_id
            # Validamos si este cumple con el valor que enviamos en el argumento
            if role_user == rol_id:
                # Si esta todo bien retornamos el siguiente paso, es decir llamamos la función continua.
                return fn(*args, **kwargs)
            return {
                'message': 'No cuentas con los permisos suficientes'
            }, HTTPStatus.FORBIDDEN
        return decorator
    return wrapper

# Como este decorador depende de que exista un usuario conectado debe ir debajo del decorador jwt_required
