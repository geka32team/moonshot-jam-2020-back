# pylint: disable=no-member,too-few-public-methods

from ..database import db


class Stat(db.Model):
    __tablename__ = 'stats'

    id = db.Column(db.Integer, primary_key=True)
    lvl = db.Column(db.Integer, default=1, nullable=False)

    hp = db.Column(db.Integer, default=50, nullable=False)

    exp = db.Column(db.Integer, default=0, nullable=False)

    strn = db.Column(db.Integer, default=7, nullable=False)
    vit = db.Column(db.Integer, default=7, nullable=False)
    dex = db.Column(db.Integer, default=7, nullable=False)
    acc = db.Column(db.Integer, default=7, nullable=False)

    dmg = db.Column(db.Integer, db.CheckConstraint(
        'dmg >= 30'), default=30, nullable=False)

    stats = db.Column(db.Integer, db.CheckConstraint(
        'stats >= 0'), default=20, nullable=False)

    bosses_defeated = db.Column(db.Integer, default=0, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id', name='stats_user_id', ondelete="CASCADE"),
        unique=True, nullable=False)
    user = db.relationship("User", back_populates="stat")
