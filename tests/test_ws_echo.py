from jsonschema import validate

from src.ws.namespace import Namespace as ns
from src.jsonschema.response.ws.echo import EchoSchema as JSONSchema


def test_echo(ws_client):
    ws_client.connect(ns.API)

    msg = {'msg': 'hello'}
    ret = ws_client.emit('echo', msg, namespace=ns.API,
                         json=True, callback=True)

    validate(schema=JSONSchema, instance=ret)

    assert ret['msg'] == msg
