# pylint: disable=no-member,too-few-public-methods

from ..database import db


class SetType(db.Model):
    __tablename__ = 'set_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)

    bonus_2items_id = db.Column(db.Integer, db.ForeignKey(
        'bonuses.id', name='set_types_bonus_2items_id'), nullable=False)
    bonus_2items = db.relationship("Bonus", foreign_keys=bonus_2items_id)

    bonus_fullset_id = db.Column(db.Integer, db.ForeignKey(
        'bonuses.id', name='set_types_bonus_fullset_id'), nullable=False)
    bonus_fullset = db.relationship("Bonus", foreign_keys=bonus_fullset_id)
