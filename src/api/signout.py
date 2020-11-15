from flask import Blueprint, request, current_app, session
from flask_json import json_response, JsonError

from ..auth import signin_required

bp = Blueprint("api.signout", __name__, url_prefix="/api")


@bp.route("/signout", methods=["POST"])
@signin_required
def signin():
    """Sign out a signed in user. Clear session."""
    data = request.get_data()

    if data:                        # pragma: no cover
        current_app.logger.error(
            f'no data is expected, but recevied {len(data)} bytes.')
        raise JsonError(message='bad request')

    session.clear()

    return json_response()
