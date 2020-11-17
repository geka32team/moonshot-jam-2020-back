import json

import pytest
from jsonschema import validate

from src.jsonschema.response.response import ResponseSchema


@pytest.mark.parametrize('data', (
    {'username': 'test', 'password': 'password'},
))
def test_signin_if_normal_request_works(api_client_unauth, data):
    response = api_client_unauth.post(
        '/api/signin', data=json.dumps(data)
    )

    assert response.status_code == 200

    validate(schema=ResponseSchema, instance=response.get_json())

    cookie = next(
        (cookie
            for cookie
            in api_client_unauth.cookie_jar
            if cookie.name == "session"),
        None
    )

    assert cookie is not None


@pytest.mark.parametrize('data,response_code', (
    ({}, 400),
    ({'username': 'test_user_124'}, 400),
    ({'password': 'secet_123'}, 400),
    ({'username': 'test_user_222', 'password': 'secREt_#23',
      'addon': 55}, 400),
    ({'username': 'test1', 'password': 'secREt_#23'}, 401),
    ({'username': 'test', 'password': 'secREt_#23'}, 401),
))
def test_signin_if_wrong_attempt_rejected(api_client_unauth, data, response_code):
    response = api_client_unauth.post(
        '/api/signin', data=json.dumps(data)
    )

    assert response.status_code == response_code

    validate(schema=ResponseSchema, instance=response.get_json())

    cookie = next(
        (cookie
            for cookie
            in api_client_unauth.cookie_jar
            if cookie.name == "session"),
        None
    )

    assert cookie is None
