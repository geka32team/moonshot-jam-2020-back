# pylint: disable=redefined-outer-name

import os
import tempfile
import json
import logging

import pytest
from flask.testing import FlaskClient
from flask_migrate import upgrade

from src import create_app
from src.database import migrate

from .populate_db import populate_db


pytest_plugins = [
    "tests.plugins.db",
]

@pytest.fixture
def app(make_record, scope="session"):
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    os.close(db_fd)

    # create the app with common test config
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": f'sqlite:///{db_path}'})

    # create the database and load test data
    with app.app_context():
        upgrade()
        populate_db(make_record)

    yield app

    # remove the temporary database
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


class APIFlaskClient(FlaskClient):
    def open(self, *args, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        return super().open(*args, **kwargs)


@pytest.fixture
def api_client_unauth(app):
    """An unauthenticated test client for the JSON API."""
    app.test_client_class = APIFlaskClient
    return app.test_client()


@pytest.fixture
def api_client(api_client_unauth):
    """A authenticated test client for the JSON API."""
    data = {'username': 'test',
            'password': 'password_test'}
    response = api_client_unauth.post(
        '/api/signin', data=json.dumps(data)
    )

    assert response.status_code == 200

    return api_client_unauth


@pytest.fixture
def ws_client_unauth(app, caplog, api_client_unauth):
    """An unauthenticated test client for the socketio API."""

    caplog.set_level(logging.DEBUG)

    socketio = app.extensions.get('socketio')
    return socketio.test_client(app, flask_test_client=api_client_unauth)


@pytest.fixture
def ws_client(app, caplog, api_client):
    """An authenticated test client for the socketio API."""

    caplog.set_level(logging.DEBUG)

    socketio = app.extensions.get('socketio')
    return socketio.test_client(app, flask_test_client=api_client)
