from flask import current_app, session, jsonify
#  import jsonschema

#  from ..jsonschema.request.ws.echo import EchoSchema as JSONSchema
from ..model.stat import Stat


def handler(msg):
    if msg:                                         # pragma: no cover
        current_app.logger.error(
            f'no data is expected, but recevied {len(data)} bytes.')
        return None

    try:
        stat = Stat.query.filter_by(
            user_id=session.get("user_id")
        ).first()
    except Exception as e:                              # pragma: no cover
        current_app.logger.error(f'DB error: {e}')
        return None

    return jsonify(stat)
