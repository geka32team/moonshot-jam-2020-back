# pylint: disable=no-member,too-few-public-methods

from sqlalchemy import UniqueConstraint

from ..database import db


class ItemTemplate(db.Model):
    __tablename__ = 'item_templates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)

    item_type_id = db.Column(db.Integer, db.ForeignKey(
        'item_types.id', name='item_templates_item_type_id',
        ondelete="CASCADE"), nullable=False)
    item_type = db.relationship("ItemType")

    set_type_id = db.Column(db.Integer, db.ForeignKey(
        'set_types.id', name='item_templates_set_type_id',
        ondelete="CASCADE"), nullable=False)
    set_type = db.relationship("SetType")

    bonus_id = db.Column(db.Integer, db.ForeignKey(
        'bonuses.id', name='item_templates_bonus_id',
        ondelete="CASCADE"), nullable=False)
    bonus = db.relationship("Bonus")

    UniqueConstraint('set_type_id', 'set_type_id')
