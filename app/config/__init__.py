from os import getenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')


class DevelopmentConfig(BaseConfig):
    pass


environment = {
    'development': DevelopmentConfig,
}
