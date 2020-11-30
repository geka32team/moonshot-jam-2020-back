from flask import current_app, session
import jsonschema

from ..jsonschema.request.ws.echo import EchoSchema as JSONSchema


def handler(msg):
    try:
        jsonschema.validate(schema=JSONSchema, instance=msg)
    except jsonschema.exceptions.ValidationError as e:      # pragma: no cover
        current_app.logger.error(f'JSON-schema validation error: {e}')
        return None

    return {'msg': msg}
