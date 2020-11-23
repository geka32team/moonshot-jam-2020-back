from src.ws.namespace import Namespace as ns


def test_connect(caplog, ws_client_unauth):
    """Test if ns.PUBLIC namespace is available"""
    assert not ws_client_unauth.is_connected(ns.PUBLIC)

    ws_client_unauth.connect(ns.PUBLIC)

    assert f"connect namespace '{ns.PUBLIC}'" in caplog.text

    assert ws_client_unauth.is_connected(ns.PUBLIC)
