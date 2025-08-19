from fastapi.testclient import TestClient


def test_planner_guardrails(client: TestClient):
    data = {
        "weight_kg": 70,
        "height_cm": 175,
        "age": 30,
        "sex": "male",
        "activity_level": 1.2,
        "goal": "maintain",
    }
    reg = client.post("/api/v1/auth/register", json={"email": "p@p.com", "password": "x"})
    token = reg.json()["access_token"]
    r = client.post(
        "/api/v1/planner/macros",
        json=data,
        headers={"Authorization": f"Bearer {token}"},
    )
    assert r.status_code == 200
    assert r.json()["fiber_g"] >= 20
