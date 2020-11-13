import sqlite3

from flask import Blueprint, request, current_app, session
from flask_json import json_response, JsonError
from werkzeug.security import check_password_hash, generate_password_hash
import jsonschema

from src.jsonschema.request.register import RegisterSchema
from src.jsonschema.request.signin import SigninSchema

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
    except jsonschema.exceptions.ValidationError as e:                      # pragma: no cover
        current_app.logger.error(f'JSON-schema validation error: {e}')
        raise JsonError(message='bad request') from e
    except Exception as e:                                                  # pragma: no cover
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request') from e

    db = get_db()

    try:
        qry = ("INSERT INTO users (username, password, ip_address, created_at) "
               "VALUES (?, ?, ?, datetime('now'))")
        params = (data['username'], generate_password_hash(data['password']),
                  request.remote_addr)
        db.execute(qry, params)

        db.commit()
    except (sqlite3.Warning, sqlite3.Error, sqlite3.DatabaseError) as e:    # pragma: no cover
        current_app.logger.error(f'DB error: {e}')
        raise JsonError(message='bad request') from e
    except Exception as e:                                                  # pragma: no cover
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request') from e

    return json_response()


@bp.route("/signin", methods=["POST"])
def signin():
    """Sign in a registered user by adding the user id to the session."""
    data = request.get_json()

    try:
        jsonschema.validate(schema=SigninSchema, instance=data)
    except jsonschema.exceptions.ValidationError as e:                      # pragma: no cover
        current_app.logger.error(f'JSON-schema validation error: {e}')
        raise JsonError(message='bad request') from e
    except Exception as e:                                                  # pragma: no cover
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request') from e

    db = get_db()

    try:
        qry = ('SELECT u.* '
               '  FROM users u '
               ' WHERE u.username = ? '
               ' LIMIT 1')
        params = (data['username'],)

        user = db.execute(qry, params).fetchone()
    except (sqlite3.Warning, sqlite3.Error, sqlite3.DatabaseError) as e:    # pragma: no cover
        current_app.logger.error(f'DB error: {e}')
        raise JsonError(message='bad request') from e
    except Exception as e:                                                  # pragma: no cover
        current_app.logger.error(f'error: {e}')
        raise JsonError(message='bad request') from e

    if user is None:
        current_app.logger.error(
            f"AUTH error: user \"{data['username']}\": not registered")
        raise JsonError(401, message='bad request')

    if not check_password_hash(user['password'], data['password']):
        current_app.logger.error(
            f"AUTH error: user \"{data['username']}\": wrong password")
        raise JsonError(401, message='bad request')

    session.clear()
    session['user_id'] = user['id']

    return json_response()
