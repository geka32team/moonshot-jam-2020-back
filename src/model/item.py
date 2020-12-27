# pylint: disable=no-member,too-few-public-methods

from ..database import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)

    item_template_id = db.Column(db.Integer, db.ForeignKey(
        'item_templates.id', name='items_item_item_template_id',
        ondelete="CASCADE"), nullable=False)
    item_template = db.relationship("ItemTemplate")

    bonus_id = db.Column(db.Integer, db.ForeignKey(
        'bonuses.id', name='items_bonus_id'), nullable=False)
    bonus = db.relationship("Bonus", foreign_keys=bonus_id)
