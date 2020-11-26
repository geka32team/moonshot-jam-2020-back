import pytest

from src.database import db


@pytest.fixture
def make_record():
    def _make_record(Model, **kwargs):
        record = Model(**kwargs)
        db.session.add(record)
        db.session.commit()

    return _make_record
