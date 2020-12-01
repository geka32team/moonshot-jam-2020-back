from flask import current_app, session
from sqlalchemy.exc import SQLAlchemyError

from ..validator.no_msg import no_msg
from ..validator.ws.stat import StatSchema as Schema
from ..model.stat import Stat


@no_msg
def handler(msg):                       # pylint: disable=unused-argument
    try:
        stat = Stat.query.filter_by(
            user_id=session.get("user_id")
        ).first()
    except SQLAlchemyError as e:        # pragma: no cover
        current_app.logger.error(f'DB error: {e}')
        return None

    schema = Schema()
    return schema.dump(stat)
