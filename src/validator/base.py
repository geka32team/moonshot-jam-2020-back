# pylint: disable=too-few-public-methods

from marshmallow import Schema, EXCLUDE


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE
