"""
Assignment Part 2: tests for GET /items/{item_id}.

Replace each pytest.fail(...) line with a real test. See test_existing.py for
examples. Every test starts with an empty database, so create any users and
items you need inside the test itself.
"""
import pytest


def test_read_item(client):
    # 1. Create a user with POST /users/
    # 2. Create an item for that user with POST /users/{user_id}/items/
    # 3. Call GET /items/{item_id} and check that:
    #    - the status code is 200
    #    - the id, title, description and owner_id match the item you created
    pytest.fail("TODO: write this test")


def test_read_missing_item_returns_404(client):
    # Call GET /items/{item_id} with an id that does not exist and check that:
    #    - the status code is 404
    #    - the response body is {"detail": "Item not found"}
    pytest.fail("TODO: write this test")


def test_read_item_with_invalid_id_returns_422(client):
    # Call GET /items/abc (an id that is not a number) and check that:
    #    - the status code is 422
    pytest.fail("TODO: write this test")
