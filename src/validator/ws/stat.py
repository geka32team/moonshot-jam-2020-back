from marshmallow import fields

from ..base import BaseSchema


class StatSchema(BaseSchema):
    lvl = fields.Integer()
    hp = fields.Integer()
    exp = fields.Integer()
    strn = fields.Integer()
    vit = fields.Integer()
    dex = fields.Integer()
    acc = fields.Integer()
    dmg = fields.Integer()
    stats = fields.Integer()
    bosses_defeated = fields.Integer()
