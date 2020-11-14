from flask import Blueprint, request, current_app, session
from flask_json import json_response, JsonError


bp = Blueprint("api.signout", __name__, url_prefix="/api")


@bp.route("/signout", methods=["POST"])
def signin():
    """Sign out a signed in user. Clear session."""
    data = request.get_data()

    if data:
        current_app.logger.error(
            f'no data is expected, but recevied {len(data)} bytes.')
        raise JsonError(message='bad request')

    session.clear()

    return json_response()
