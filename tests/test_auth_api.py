import pytest
import json
from jsonschema import validate

from src.jsonschema.response.response import ResponseSchema
from src.jsonschema.response.error import ErrorSchema
from src.db import get_db


def test_register_if_only_POST_is_allowed(api_client, app):
    assert api_client.get('/api/register').status_code == 405


@pytest.mark.parametrize('data', (
    {'username': 'test_user_123', 'password': 'secREt_#23'},
    {'username': 'test_user_124', 'password': 'sEcret_123'},
    {'username': 'test_12a3', 'password': 'secet_123'}
))
def test_register_if_normal_request_works(api_client, app, data):
    response = api_client.post(
        '/api/register', data=json.dumps(data)
    )

    assert response.status_code == 200

    validate(schema=ResponseSchema, instance=response.get_json())

    # check if record has been added
    with app.app_context():
        assert get_db().execute(
            'SELECT * '
              'FROM users '
             'WHERE username = ?',
            (data['username'],)
        ).fetchone() is not None


@pytest.mark.parametrize('data', (
    {'username': 'test', 'password': 'secREt_#23'},    # duplicate
    {},
    {'username': 'test_user_124'},
    {'password': 'secet_123'},
    {'username': 'test_user_222', 'password': 'secREt_#23', 'addon': 55},
))
def test_register_if_wrong_data_rejected(api_client, app, data):
    response = api_client.post(
        '/api/register', data=json.dumps(data)
    )

    assert response.status_code == 400

    validate(schema=ErrorSchema, instance=response.get_json())
