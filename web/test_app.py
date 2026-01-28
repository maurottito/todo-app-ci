import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"ok"


def test_index(client):
    """Test index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Todo API" in response.data


def test_index_has_form(client):
    """Test index page has form"""
    response = client.get("/")
    assert b"<form" in response.data


def test_index_has_link(client):
    """Test index page has view link"""
    response = client.get("/")
    assert b"/list" in response.data


def test_index_has_button(client):
    """Test index page has button"""
    response = client.get("/")
    assert b"button" in response.data
