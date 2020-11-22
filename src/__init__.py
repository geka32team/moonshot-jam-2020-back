import os
from distutils.util import strtobool

from flask import Flask
from flask_json import FlaskJSON
from flask_cors import CORS
from flask_socketio import SocketIO

from . import api
from . import db
from . import auth
from . import ws


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True,
                static_folder='../static')

    FlaskJSON(app)
    CORS(app, origins=['http://127.0.0.1:5000',
                       'http://127.0.0.1:3000',
                       'http://lubuntu-18:3000',
                       'http://localhost:3000'],
         supports_credentials=True,
         )

    socketio_logger = bool(strtobool(os.getenv("SOCKETIO_LOGGER", "False")))
    socketio = SocketIO(app,
        engineio_logger=socketio_logger,
        cors_allowed_origins=['http://127.0.0.1:5000',
                              'http://127.0.0.1:3000',
                              'http://lubuntu-18:3000',
                              'http://localhost:3000'],
        cors_credentials=True)

    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "moonnymathics.sqlite"),
    )

    # Help Chrome browser to use CORS cookies
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='None',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        print(f"creating DATABASE={app.config['DATABASE']}")
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    db.init_app(app)

    # init and register authentication helpers
    auth.init_app(app)

    # api handlers
    api.register_all(app)

    # websockets handlers
    ws.register_all(socketio)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    #  app.add_url_rule("/", endpoint="index")

    return app
