from flask import Blueprint, request, current_app, session
from flask_json import json_response, JsonError
from flask_socketio import disconnect

from ..auth import signin_required
from ..validator.no_post_data import no_post_data
from ..ws.namespace import Namespace as ns

bp = Blueprint("api.signout", __name__, url_prefix="/api")


@bp.route("/signout", methods=["POST"])
@signin_required
@no_post_data
def signout():
    """Sign out a signed in user. Clear session."""

    if session.get("ws_sid") is not None:
        disconnect(session.get("ws_sid"), ns.API)

    session.clear()

    return json_response()
