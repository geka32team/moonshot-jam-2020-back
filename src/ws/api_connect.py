from flask_socketio import ConnectionRefusedError   # pylint: disable=redefined-builtin
from flask import current_app, request, session


def handler():
    user_id = session.get("user_id")
    user_username = session.get("user_username")

    if user_id is None:
        raise ConnectionRefusedError('unauthorized')

    current_app.logger.debug(f"user '{user_username}' has connected '{request.namespace}'")
