import json
import pytest
from jsonschema import validate

from src.jsonschema.response.response import ResponseSchema


def test_signout_unauthenticated(api_client):
    response = api_client.post(
        '/api/signout'
    )

    assert response.status_code == 401

    validate(schema=ResponseSchema, instance=response.get_json())

    cookie = next(
        (cookie
            for cookie
            in api_client.cookie_jar
            if cookie.name == "session"),
        None
    )

    assert cookie is None


@pytest.mark.parametrize('scenario', (
    (
        {'endpoint': '/api/signin',
         'data': {'username': 'test',
                  'password': 'password'},
         'response_code': 200,
         'session_exists': True},
        #
        {'endpoint': '/api/signout',
         'data': None,
         'response_code': 200,
         'session_exists': False},
    ),
))
def test_signout_scenarios(api_client, scenario):
    for step in scenario:
        data = json.dumps(step['data']) if step['data'] else None
        response = api_client.post(
            step['endpoint'], data=data
        )

        assert response.status_code == step['response_code']

        validate(schema=ResponseSchema, instance=response.get_json())

        cookie = next(
            (cookie
                for cookie
                in api_client.cookie_jar
                if cookie.name == "session"),
            None
        )

        assert (cookie is not None) == step['session_exists']
