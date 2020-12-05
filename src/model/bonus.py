# pylint: disable=no-member,too-few-public-methods

from ..database import db


class Bonus(db.Model):
    __tablename__ = 'bonuses'

    id = db.Column(db.Integer, primary_key=True)

    hp = db.Column(db.Integer, default=0, nullable=False)
    strn = db.Column(db.Integer, default=0, nullable=False)
    vit = db.Column(db.Integer, default=0, nullable=False)
    dex = db.Column(db.Integer, default=0, nullable=False)
    acc = db.Column(db.Integer, default=0, nullable=False)
    dmg = db.Column(db.Integer, default=0, nullable=False)

    crit_chance = db.Column(db.Integer, default=0, nullable=False)
    crit_power = db.Column(db.Integer, default=0, nullable=False)
    time = db.Column(db.Float, default=0, nullable=False)
