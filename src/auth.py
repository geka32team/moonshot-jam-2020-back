import functools
from flask import current_app, session, g
from flask_json import JsonError

from .api.signin import bp
from .db import get_db


@bp.before_app_request
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
