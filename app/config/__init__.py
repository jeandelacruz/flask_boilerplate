from os import getenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False


class DevelopmentConfig(BaseConfig):
    pass


environment = {
    'development': DevelopmentConfig,
}
