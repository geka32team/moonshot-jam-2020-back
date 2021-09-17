# pylint: disable=no-member,too-few-public-methods

from ..database import db


class RarityType(db.Model):
    __tablename__ = 'rarity_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
