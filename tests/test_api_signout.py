import json
import pytest
from jsonschema import validate

from src.jsonschema.response.response import ResponseSchema
from src.ws.namespace import Namespace as ns


def test_signout_unauthenticated(api_client_unauth):
    response = api_client_unauth.post(
        '/api/signout'
    )

    assert response.status_code == 401

    validate(schema=ResponseSchema, instance=response.get_json())


def test_signout_authenticated(api_client):
    response = api_client.post(
        '/api/signout'
    )

    assert response.status_code == 200

    validate(schema=ResponseSchema, instance=response.get_json())


def test_signout_authenticated_with_data(api_client):
    response = api_client.post(
        '/api/signout',
        data=json.dumps({'dummy': 'data'})
    )

    assert response.status_code == 400

    validate(schema=ResponseSchema, instance=response.get_json())


@pytest.mark.parametrize('scenario', (
    (
        {'endpoint': '/api/signin',
         'data': {'username': 'test',
                  'password': 'password_test'},
         'response_code': 200,
         'session_exists': True,
         'ws_available': True},
        #
        {'endpoint': '/api/signout',
         'data': None,
         'response_code': 200,
         'session_exists': False,
         'ws_available': False},
    ),
))
def test_signout_ws_client(
        caplog, api_client_unauth, ws_client_unauth, scenario):
    client = ws_client_unauth

    for step in scenario:
        caplog.clear()

        data = json.dumps(step['data']) if step['data'] else None
        response = api_client_unauth.post(
            step['endpoint'], data=data
        )

        assert response.status_code == step['response_code']

        validate(schema=ResponseSchema, instance=response.get_json())

        client.connect(ns.API)

        msg = {'msg': 'hello'}
        ret = client.emit('echo', msg, namespace=ns.API,
                          json=True, callback=True)

        if step['ws_available']:
            assert ret['msg'] == msg
        else:
            assert f'{client.sid} is not connected to namespace {ns.API}' in caplog.text
