# pylint: disable=no-member,too-few-public-methods

from datetime import datetime


from ..database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    ip_address = db.Column(db.String(39), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    stat = db.relationship("Stat", uselist=False, back_populates="user")
