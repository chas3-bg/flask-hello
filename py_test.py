import pytest
from app import app  # Import the Flask app from your application

@pytest.fixture
def client():
    # Set up a test client
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    # Send a GET request to the "/hello" route
    response = client.get("/")
    assert response.status_code == 200  # Check if the status code is 200
    assert response.data == b"Hello from flask"# Check if the response data matches "hello"

def test_secret(client):
    response = client.get('/secret')
    assert response.status_code == 200
    assert response.data == b'Super secret path'

