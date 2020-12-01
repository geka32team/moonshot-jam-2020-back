from flask import Blueprint, request, current_app
from flask_json import json_response, JsonError
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError
import jsonschema

from ..database import db
from ..model.user import User
from ..model.stat import Stat
from ..jsonschema.request.register import RegisterSchema as JSONSchema
from ..validator.api.register import RegisterSchema as ValidationScheama


bp = Blueprint("api.register", __name__, url_prefix="/api")


@bp.route("/register", methods=["POST"])
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """

    data = request.get_json()

    try:
        jsonschema.validate(schema=JSONSchema, instance=data)
    except jsonschema.exceptions.ValidationError as e:      # pragma: no cover
        current_app.logger.error(f'JSON-schema validation error: {e}')
        raise JsonError(message='bad request') from e

    try:
        ValidationScheama().load(data)
    except ValidationError as e:
        current_app.logger.error(f'validation error: {e}')
        raise JsonError(message='bad request') from e

    try:
        if request.headers.getlist("X-Forwarded-For"):      # pragma: no cover
            ip_address = request.headers.getlist("X-Forwarded-For")[-1]
        else:                                   # pragma: no cover
            ip_address = request.remote_addr

        user = User(username=data['username'],
                    password=generate_password_hash(data['password']),
                    ip_address=ip_address)
        db.session.add(user)                    # pylint: disable=no-member
        db.session.flush()                      # pylint: disable=no-member

        stat = Stat(user_id=user.id)
        db.session.add(stat)                    # pylint: disable=no-member

        db.session.commit()                     # pylint: disable=no-member
    except SQLAlchemyError as e:
        current_app.logger.error(f'DB error: {e}')
        raise JsonError(message='bad request') from e

    return json_response()
