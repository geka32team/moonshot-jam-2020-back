from src.ws.namespace import Namespace as ns


def test_connect_unauth(caplog, ws_client_unauth):
    """Test if ns.API namespace is unavailable"""
    client = ws_client_unauth

    client.connect(ns.API)
    client.send('test_connect_unauth',
                namespace=ns.API, callback=True)

    assert f'{client.sid} is not connected to namespace {ns.API}' in caplog.text


def test_connect(caplog, ws_client):
    """Test if ns.API namespace is unavailable"""

    assert not ws_client.is_connected(ns.API)

    ws_client.connect(ns.API)

    assert ws_client.is_connected(ns.API)

    assert f"connect '{ns.API}', user: 'test'" in caplog.text
