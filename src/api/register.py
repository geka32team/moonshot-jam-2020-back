import sqlite3

from flask import Blueprint, request, current_app
from flask_json import json_response, JsonError
from werkzeug.security import generate_password_hash
from marshmallow import ValidationError
import jsonschema

from ..db import get_db
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
    except Exception as e:                                  # pragma: no cover
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request') from e

    try:
        ValidationScheama().load(data)
    except ValidationError as e:
        current_app.logger.error(f'validation error: {e}')
        raise JsonError(message='bad request') from e

    db = get_db()

    try:
        qry = ("INSERT INTO users "
               "       (username, password, ip_address, created_at) "
               "VALUES (?, ?, ?, datetime('now'))")
        params = (data['username'], generate_password_hash(data['password']),
                  request.remote_addr)
        db.execute(qry, params)

        db.commit()
    except (sqlite3.Warning, sqlite3.Error,
            sqlite3.DatabaseError) as e:                    # pragma: no cover
        current_app.logger.error(f'DB error: {e}')
        raise JsonError(message='bad request') from e
    except Exception as e:                                  # pragma: no cover
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request') from e

    return json_response()
