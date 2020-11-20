from src.ws.namespace import Namespace as ns


def test_echo(caplog, ws_client):
    ws_client.connect(ns.API)

    ret = ws_client.emit('echo', 'hello', namespace=ns.API, callback=True)

    assert 'echo: hello' in ret
