from jsonschema import validate

from src.ws.namespace import Namespace as ns
from src.jsonschema.response.ws.getCharacterInfo import GetCharacterInfoSchema as JSONSchema


def test_get_character_info(ws_client):
    ws_client.connect(ns.API)

    msg = None
    ret = ws_client.emit('getCharacterInfo', msg, namespace=ns.API,
                         json=True, callback=True)

    validate(schema=JSONSchema, instance=ret)

    assert ret['msg'] == msg
