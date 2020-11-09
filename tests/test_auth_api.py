import json

from src.db import get_db

def test_register(api_client, app):
    assert api_client.get('/api/register').status_code == 405

    data = {'username': 'test_user_123',
            'password': 'secret'}
    response = api_client.post(
        '/api/register', data=json.dumps(data)
    )

    with app.app_context():
        assert get_db().execute(
            "SELECT * "
              "FROM users "
             "WHERE username = 'test_user_123'",
        ).fetchone() is not None
