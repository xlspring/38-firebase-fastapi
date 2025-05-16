from fastapi.testclient import TestClient
import pytest
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Demo API"}

def test_create_item():
    item_data = {
        "name": "Test Item",
        "description": "This is a test item",
        "price": 9.99
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert data["price"] == item_data["price"]
    assert "id" in data
    return data["id"]

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_item():
    # First create an item
    item_id = test_create_item()
    
    # Then retrieve it
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id

def test_delete_item():
    # First create an item
    item_id = test_create_item()
    
    # Then delete it
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404 