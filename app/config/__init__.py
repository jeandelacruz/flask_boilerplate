from os import getenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    # Rastreo de modificaciones como eventos, consumo de memoria alta por eso lo desactivamos
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


environment = {
    'development': DevelopmentConfig,
}
