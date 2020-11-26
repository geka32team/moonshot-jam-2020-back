import pytest
import json
from jsonschema import validate

from src.model.user import User
from src.jsonschema.response.response import ResponseSchema
from src.jsonschema.response.error import ErrorSchema


@pytest.mark.parametrize('data', (
    {'username': 'test_user_123', 'password': 'secREt_#23'},
    {'username': 'test_user_124', 'password': 'sEcret_123'},
    {'username': 'test_12a3', 'password': 'secet_123'},
    {'username': 'Жtest_12a3', 'password': 'secet_123'},
    {'username': 'test_12a3Ж', 'password': 'secet_123'},
    {'username': '3 test_12a3', 'password': 'secet_123'},
))
def test_register_if_normal_request_works(api_client_unauth, app, data):
    response = api_client_unauth.post(
        '/api/register', data=json.dumps(data)
    )

    assert response.status_code == 200

    validate(schema=ResponseSchema, instance=response.get_json())

    # check if record has been added
    with app.app_context():
        user = User.query.filter_by(
            username=data.get('username'),
            ip_address='127.0.0.1'
            ).first()

        assert user is not None


@pytest.mark.parametrize('data,is_duplicate', (
    ({'username': 'admin', 'password': 'secREt_#23'}, True),
    ({'username': ' test333', 'password': 'secREt_#23'}, False),
    ({'username': '\ttest333', 'password': 'secREt_#23'}, False),
    ({'username': '\rtest333', 'password': 'secREt_#23'}, False),
    ({'username': '\ntest333', 'password': 'secREt_#23'}, False),
    ({'username': 'test333 ', 'password': 'secREt_#23'}, False),
    ({'username': 'test333\t', 'password': 'secREt_#23'}, False),
    ({'username': 'test333\r', 'password': 'secREt_#23'}, False),
    ({'username': 'test333\n', 'password': 'secREt_#23'}, False),
    ({}, False),
    ({'username': 'test_user_124'}, False),
    ({'password': 'secet_123'}, False),
    ({'username': 'test_user_222', 'password': 'secREt_#23',
      'addon': 55}, False),
))
def test_register_if_wrong_data_rejected(
        api_client_unauth, app, data, is_duplicate):
    response = api_client_unauth.post(
        '/api/register', data=json.dumps(data)
    )

    assert response.status_code == 400

    validate(schema=ErrorSchema, instance=response.get_json())

    if not is_duplicate:
        # check if record has not been added
        with app.app_context():
            user = User.query.filter_by(
                username=data.get('username', None)
                ).first()

            assert user is None
