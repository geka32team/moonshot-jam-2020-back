from src.ws.namespace import Namespace as ns


def test_connect(caplog, ws_client_unauth):
    """Test if ns.GLOABLA namespace is available"""

    ws_client_unauth.connect(ns.GLOBAL)

    assert f"connect namespace '{ns.GLOBAL}'" in caplog.text

    assert ws_client_unauth.is_connected(ns.GLOBAL)
