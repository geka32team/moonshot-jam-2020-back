from flask import Blueprint, url_for, request, current_app
from flask_json import json_response, JsonError
from werkzeug.security import check_password_hash, generate_password_hash
import jsonschema
import sqlite3

from src.jsonschema.request.register import RegisterSchema

from .db import get_db


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/register", methods=["POST"])
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """

    data = request.get_json()

    try:
        jsonschema.validate(schema=RegisterSchema, instance=data)
    except jsonschema.exceptions.ValidationError as e:
        current_app.logger.error(f'JSON-schema validation error: {e}')
        raise JsonError(message='bad request')
    except Exception as e:
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request')

    db = get_db()

    try:
        qry = ("INSERT INTO users (username, password, ip_address, created_at) "
               "VALUES (?, ?, ?, datetime('now'))")
        params = (data['username'], generate_password_hash(data['password']), 'ip')
        db.execute(qry, params)

        db.commit()
    except (sqlite3.Warning, sqlite3.Error, sqlite3.DatabaseError) as e:
        current_app.logger.error(f'DB error: {e}')
        raise JsonError(message='bad request')
    except Exception as e:
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request')

    return json_response()
