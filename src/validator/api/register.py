import re
from marshmallow import fields, validates, ValidationError

from ..base import BaseSchema


class RegisterSchema(BaseSchema):
    username = fields.Str()

    @validates('username')
    def validate_username(self, value):     # pylint: disable=no-self-use
        if re.search(r'\s$', value, re.MULTILINE):
            raise ValidationError(f"inivalid character in value '{value}'")
