# pylint: disable=too-few-public-methods

import pytest


from src.database import db
from src.model.user import User


def test_db_connection(app):
    assert db is not None

    #  with pytest.raises(sqlite3.ProgrammingError) as e:
    with app.app_context():
        me = User(username='admin3', password='password', ip_address='127.0.0.1')
        db.session.add(me)
        db.session.commit()

        assert me.id == 1

    #  assert "closed" == me.id
