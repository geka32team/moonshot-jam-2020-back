from flask import current_app
import jsonschema

from ..jsonschema.request.ws.echo import EchoSchema as JSONSchema


def handler(msg):
    try:
        jsonschema.validate(schema=JSONSchema, instance=msg)
    except jsonschema.exceptions.ValidationError as e:      # pragma: no cover
        current_app.logger.error(f'JSON-schema validation error: {e}')
        return None

    current_app.logger.debug(f"msg: {msg}")
    return {'msg': msg}
