"""
Example tests for the endpoints that already exist.

Read these before writing your own tests in test_items.py. They show how to
call the API with the `client` fixture and check what comes back.
"""


def test_test_endpoint(client):
    response = client.get("/test")
    assert response.status_code == 200


def test_create_user(client):
    response = client.post("/users/", json={"email": "rhett@bu.edu", "password": "terriers"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "rhett@bu.edu"
    assert data["is_active"] is True
    assert data["items"] == []


def test_create_user_with_duplicate_email_returns_400(client):
    client.post("/users/", json={"email": "rhett@bu.edu", "password": "terriers"})
    response = client.post("/users/", json={"email": "rhett@bu.edu", "password": "different"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}


def test_read_missing_user_returns_404(client):
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_create_item_for_user(client):
    user = client.post("/users/", json={"email": "rhett@bu.edu", "password": "terriers"}).json()
    response = client.post(
        f"/users/{user['id']}/items/",
        json={"title": "Laptop", "description": "For CS501"},
    )
    assert response.status_code == 200
    item = response.json()
    assert item["title"] == "Laptop"
    assert item["description"] == "For CS501"
    assert item["owner_id"] == user["id"]
