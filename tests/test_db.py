# pylint: disable=too-few-public-methods

import pytest

from src.database import db
from src.model.user import User


def test_db_connection(app):
    assert db is not None

    #  with pytest.raises(sqlite3.ProgrammingError) as e:
    with app.app_context():
        admin = User.query.filter_by(username='admin').first()
        assert admin.id == 1

        admin2 = User.query.filter_by(username='admin2').first()
        assert admin2.id == 2

        admin3 = User.query.filter_by(username='admin3').first()
        assert admin3 == None
