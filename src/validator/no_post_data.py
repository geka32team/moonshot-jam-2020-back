import functools
from flask import current_app, request
from flask_json import JsonError


def no_post_data(view):
    """Decorator that checks if POST request is empty."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if request.content_length:
            current_app.logger.error(
                f'no data is expected, but recevied {request.content_length} bytes.')
            raise JsonError(message='bad request')

        return view(**kwargs)

    return wrapped_view
