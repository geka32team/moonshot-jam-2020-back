import os
from distutils.util import strtobool

from flask import Flask
from flask_json import FlaskJSON
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_session import Session

from . import config
from . import database
from . import model
from . import auth
from . import api
from . import ws


def create_app(testing_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    if testing_config is not None:              # pragma: no cover
        app_config = config.TestingConfig(app)
    elif app.config["ENV"] == "production":     # pragma: no cover
        app_config = config.ProductionConfig(app)
    else:                                       # pragma: no cover
        app_config = config.DevelopmentConfig(app)

    app.config.from_object(app_config)

    Session(app)

    FlaskJSON(app)
    CORS(app, origins=app.config["CORS_ALLOWED_ORIGINS"],
         supports_credentials=True,
         )

    socketio = SocketIO(
        app,
        manage_session=False,
        engineio_logger=app.config["SOCKETIO_LOGGER"],
        cors_allowed_origins=app.config["CORS_ALLOWED_ORIGINS"],
        cors_credentials=True)

    if testing_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config
        app.config.update(testing_config)


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # init database here when app's config is ready
    database.db.init_app(app)
    database.migrate.init_app(app, database.db)

    # init and register authentication helpers
    auth.init_app(app)

    # api handlers
    api.register_all(app)

    # websockets handlers
    ws.register_all(socketio)

    return app
