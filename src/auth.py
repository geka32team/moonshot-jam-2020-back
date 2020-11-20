import functools
from flask import current_app, session, g
from flask_json import JsonError
from flask_socketio import disconnect

from .db import get_db


def load_signed_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = (get_db().execute(
            "SELECT * FROM users WHERE id = ? LIMIT 1",
            (user_id,)).fetchone())


def signin_required(view):
    """Decorator that checks if user has signed in."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            current_app.logger.error(
                'AUTH error: signin is required')
            raise JsonError(401, message='bad request')

        return view(**kwargs)

    return wrapped_view


def ws_auth_required(handler):
    """Decorator that checks if socketio client is authenticated."""

    @functools.wraps(handler)
    def wrapped(*args, **kwargs):
        user_id = session.get("user_id")

        if user_id is None:
            current_app.logger.debug("unauthorized")
            disconnect()

            return None

        return handler(*args, **kwargs)

    return wrapped


def init_app(app):
    app.before_request(load_signed_in_user)
