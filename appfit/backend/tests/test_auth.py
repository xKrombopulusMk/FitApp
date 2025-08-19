from fastapi.testclient import TestClient


def test_register_and_login(client: TestClient):
    data = {"email": "u@example.com", "password": "secret"}
    r = client.post("/api/v1/auth/register", json=data)
    assert r.status_code == 200
    token = r.json()["access_token"]

    r = client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
