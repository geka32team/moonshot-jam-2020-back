import os
from distutils.util import strtobool


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "dev"
    if os.getenv("SECRET_KEY") is not None:
        SECRET_KEY = os.getenv("SECRET_KEY")

    CORS_ALLOWED_ORIGINS = '*'
    if os.getenv("CORS_ALLOWED_ORIGINS") is not None:
        CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS")

    SOCKETIO_LOGGER = bool(strtobool(
        os.getenv("SOCKETIO_LOGGER", "False")))

    SQLALCHEMY_TRACK_MODIFICATIONS = bool(strtobool(
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False")))


    def __init__(self, app):
        self.SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(
            app.instance_path, "moonnymathics.sqlite")
        if os.getenv("DATABASE_URL") is not None:
            self.SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
        if os.getenv("SQLALCHEMY_DATABASE_URI") is not None:
            self.SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


class ProductionConfig(Config):
    # Help Chrome browser to use CORS cookies
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'


class DevelopmentConfig(Config):
    DEBUG = True

    # Help Chrome browser to use CORS cookies
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'

    CORS_ALLOWED_ORIGINS = [
        'http://127.0.0.1:5000',
        'http://127.0.0.1:3000',
        'http://localhost:5000',
        'http://localhost:3000'] 

    SOCKETIO_LOGGER = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    SOCKETIO_LOGGER = True
