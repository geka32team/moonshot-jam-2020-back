from flask_socketio import ConnectionRefusedError   # pylint: disable=redefined-builtin
from flask import current_app, request

from .namespace import Namespace as ns


def handler():
    current_app.logger.debug(f"connect namespace '{request.namespace}'")
