from jsonschema import validate

from src.ws.namespace import Namespace as ns
from src.jsonschema.response.ws.get_character_info import GetCharacterInfoSchema as JSONSchema


def test_get_character_info_with_data(ws_client, caplog):
    ws_client.connect(ns.API)

    msg = {'msg': 'hello'}
    ws_client.emit('getCharacterInfo', msg, namespace=ns.API,
                   json=True, callback=True)

    assert f'{ws_client.sid}: getCharacterInfo: no message is expected' in caplog.text


def test_get_character_info(ws_client):
    ws_client.connect(ns.API)

    msg = None
    ret = ws_client.emit('getCharacterInfo', msg, namespace=ns.API,
                         json=True, callback=True)

    validate(schema=JSONSchema, instance=ret)
