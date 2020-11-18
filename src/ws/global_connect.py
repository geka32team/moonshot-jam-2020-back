from flask_socketio import ConnectionRefusedError   # pylint: disable=redefined-builtin
from flask import current_app, request

from .namespace import Namespace as ns


def handler():
    current_app.logger.debug(f"connect namespace '{request.namespace}'")
    if request.namespace not in (
            getattr(ns, k) for k in dir(ns) if not k.startswith('__')):
        current_app.logger.debug(
            f"namespace '{request.namespace}' is unavailabe")
        raise ConnectionRefusedError('unavailabe')
