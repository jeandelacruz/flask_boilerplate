from os import getenv
from datetime import timedelta


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    # Rastreo de modificaciones como eventos, consumo de memoria alta por eso lo desactivamos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('SECRET_KEY')
    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = getenv('MAIL_PORT')
    MAIL_USE_TLS = getenv('MAIL_USE_TLS')
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')


class DevelopmentConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=1)
    MAIL_DEBUG = True


class ProductionConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=3)
    MAIL_DEBUG = False


environment = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
