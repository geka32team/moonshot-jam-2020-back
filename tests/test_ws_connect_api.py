import logging

from src.ws.namespace import Namespace as ns


def test_connect_unauth(caplog, ws_client_unauth):
    """Test if ns.API namespace is unavailable"""
    assert not ws_client_unauth.is_connected(ns.API)

    ws_client_unauth.connect(ns.API)

    ret = ws_client_unauth.send('test_connect_unauth', namespace=ns.API, callback=True)

    assert 'is not connected to namespace /api' in caplog.text


def test_connect(caplog, ws_client):
    """Test if ns.API namespace is unavailable"""

    caplog.set_level(logging.DEBUG)

    assert not ws_client.is_connected(ns.API)

    ws_client.connect(ns.API)

    assert ws_client.is_connected(ns.API)

    assert "user 'test' has connected '/api'" in caplog.text
