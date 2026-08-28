import pytest
from server import app


@pytest.fixture
def client():
  app.config["TESTING"] = True
  with app.test_client() as client:
    yield client


def test_valid_transfer(client):
  response = client.post(
      "/transfer",
      json={"sender_id": "user_1", "recipient_id": "user_2", "amount": 100},
  )
  assert response.status_code == 200


def test_negative_transfer_vulnerability(client):
  # Exploit attempt: Negative value should fail
  response = client.post(
      "/transfer",
      json={"sender_id": "user_1", "recipient_id": "user_2", "amount": -500},
  )
  # This assertion fails in the unpatched code (reproducing the vulnerability)
  assert response.status_code == 400