from flask import Blueprint, request, current_app, session
from flask_json import json_response, JsonError
from werkzeug.security import check_password_hash
from sqlalchemy.exc import SQLAlchemyError
import jsonschema

from ..model.user import User
from ..jsonschema.request.signin import SigninSchema as JSONSchema


bp = Blueprint("api.signin", __name__, url_prefix="/api")


@bp.route("/signin", methods=["POST"])
def signin():
    """Sign in a registered user by adding the user id to the session."""
    data = request.get_json()

    try:
        jsonschema.validate(schema=JSONSchema, instance=data)
    except jsonschema.exceptions.ValidationError as e:  # pragma: no cover
        current_app.logger.error(f'JSON-schema validation error: {e}')
        raise JsonError(message='bad request') from e

    try:
        user = User.query.filter_by(
            username=data.get('username')
        ).first()
    except SQLAlchemyError as e:                        # pragma: no cover
        current_app.logger.error(f'DB error: {e}')
        raise JsonError(message='bad request') from e

    if user is None:
        current_app.logger.error(
            f"AUTH error: user \"{data['username']}\": not registered")
        raise JsonError(401, message='bad request')

    if not check_password_hash(user.password, data['password']):
        current_app.logger.error(
            f"AUTH error: user \"{data['username']}\": wrong password")
        raise JsonError(401, message='bad request')

    session.clear()
    session['user_id'] = user.id
    session['user_username'] = user.username

    return json_response()
