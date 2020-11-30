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

    cookie = next(
        (cookie
            for cookie
            in api_client_unauth.cookie_jar
            if cookie.name == "session"),
        None
    )

    assert cookie is None


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
def test_signout_scenarios(caplog, api_client_unauth, ws_client_unauth, scenario):
    for step in scenario:
        data = json.dumps(step['data']) if step['data'] else None
        response = api_client_unauth.post(
            step['endpoint'], data=data
        )

        assert response.status_code == step['response_code']

        validate(schema=ResponseSchema, instance=response.get_json())

        cookie = next(
            (cookie
                for cookie
                in api_client_unauth.cookie_jar
                if cookie.name == "session"),
            None
        )

        assert (cookie is not None) == step['session_exists']

        ws_client_unauth.connect(ns.API)

        if step['ws_available']:
            assert f"connect '{ns.API}', user: 'test'" in caplog.text

            msg = {'msg': 'hello'}
            ret = ws_client_unauth.emit('echo', msg, namespace=ns.API,
                                json=True, callback=True)
            assert ret['msg'] == msg
        else:
            assert f'is not connected to namespace {ns.API}' in caplog.text

        caplog.clear()
