import functools
from flask import current_app, request


def no_msg(handler):
    """Decorator that checks if WS message is empty."""

    @functools.wraps(handler)
    def wrapped_view(msg):
        if msg is not None:
            current_app.logger.error(
                f'{request.sid}: {request.event["message"]}: no message is expected')
            return None

        return handler(msg)

    return wrapped_view
