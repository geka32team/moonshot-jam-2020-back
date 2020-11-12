import pytest
import json
from jsonschema import validate

from src.jsonschema.response.response import ResponseSchema
from src.jsonschema.response.error import ErrorSchema
from src.db import get_db


@pytest.mark.parametrize('endpoint,methods', (
    ('/api/register', {'POST'}),
    ('/api/signin', {'POST'})
))
def test_if_http_method_is_allowed(api_client, app, endpoint, methods):
    all_methods = {'GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'PATCH'}
    for method in all_methods - methods:
        assert api_client.open(endpoint, method=method).status_code == 405


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
             'WHERE username = ? AND ip_address = ?',
            (data.get('username'), '127.0.0.1')
        ).fetchone() is not None


@pytest.mark.parametrize('data,is_duplicate', (
    ({'username': 'test', 'password': 'secREt_#23'}, True),
    ({}, False),
    ({'username': 'test_user_124'}, False),
    ({'password': 'secet_123'}, False),
    ({'username': 'test_user_222', 'password': 'secREt_#23', 'addon': 55}, False)
))
def test_register_if_wrong_data_rejected(api_client, app, data, is_duplicate):
    response = api_client.post(
        '/api/register', data=json.dumps(data)
    )

    assert response.status_code == 400

    validate(schema=ErrorSchema, instance=response.get_json())

    if not is_duplicate:
        # check if record has not been added
        with app.app_context():
            assert get_db().execute(
                'SELECT * '
                'FROM users '
                'WHERE username = ?',
                (data.get('username', None),),
            ).fetchone() is None


@pytest.mark.parametrize('data', (
    #  {'username': 'test_user_123', 'password': 'secREt_#23'},
    #  {'username': 'test_user_124', 'password': 'sEcret_123'},
    {'username': 'test', 'password': 'test'}
))
def test_signin_if_normal_request_works(api_client, app, data):
    response = api_client.post(
        '/api/signin', data=json.dumps(data)
    )

    assert response.status_code == 200

    validate(schema=ResponseSchema, instance=response.get_json())
