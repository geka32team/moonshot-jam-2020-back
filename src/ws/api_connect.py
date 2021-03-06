from flask_socketio import ConnectionRefusedError   # pylint: disable=redefined-builtin
from flask import current_app, request, session


def handler():
    user_id = session.get("user_id")
    user_username = session.get("user_username")

    if user_id is None:
        raise ConnectionRefusedError('unauthorized')

    session['ws_sid'] = request.sid

    current_app.logger.debug(
        f"connect '{request.namespace}', user: '{user_username}'")
