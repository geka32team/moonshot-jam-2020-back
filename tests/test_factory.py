from flask import Flask

from src import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_index(client):
    """Test if index file is absent"""
    response = client.get("/")
    assert response.status_code == 404
