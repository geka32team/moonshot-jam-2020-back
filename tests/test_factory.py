from src import create_app
from src.ws.namespace import Namespace as ns


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_index(client):
    """Test if index file is absent"""
    response = client.get("/")
    assert response.status_code == 404


def test_api_index(api_client_unauth):
    """Test if API index method is absent"""
    response = api_client_unauth.post("/")
    assert response.status_code == 404


def test_ws(ws_client_public):
    """Test if global namespace is not available"""
    assert not ws_client_public.is_connected(ns.PUBLIC)

    ws_client_public.connect(ns.PUBLIC)

    assert ws_client_public.is_connected(ns.PUBLIC)
