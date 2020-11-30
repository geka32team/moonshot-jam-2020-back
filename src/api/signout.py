from flask import Blueprint, request, current_app, session
from flask_json import json_response, JsonError
from flask_socketio import disconnect

from ..auth import signin_required
from ..ws.namespace import Namespace as ns

bp = Blueprint("api.signout", __name__, url_prefix="/api")


@bp.route("/signout", methods=["POST"])
@signin_required
def signout():
    """Sign out a signed in user. Clear session."""
    data = request.get_data()

    if data:                        # pragma: no cover
        current_app.logger.error(
            f'no data is expected, but recevied {len(data)} bytes.')
        raise JsonError(message='bad request')

    disconnect(session.get("ws_sid"), ns.API)

    session.clear()

    return json_response()
