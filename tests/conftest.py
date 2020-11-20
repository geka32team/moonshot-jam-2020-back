# pylint: disable=redefined-outer-name

import os
import tempfile
import json
import logging

import pytest
from flask.testing import FlaskClient

from src import create_app
from src.db import init_db, get_db


# read in SQL for populating test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    _data_sql = f.read().decode("utf8")


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    # create the app with common test config
    app = create_app({"TESTING": True, "DATABASE": db_path})

    # create the database and load test data
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()


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
            'password': 'password'}
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
