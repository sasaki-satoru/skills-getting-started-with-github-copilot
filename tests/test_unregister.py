def test_unregister_success(client):
    response = client.delete(
        "/activities/Chess Club/unregister", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 200
    assert "michael@mergington.edu" not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    response = client.delete(
        "/activities/Unknown Club/unregister", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 404


def test_unregister_not_signed_up_returns_400(client):
    response = client.delete(
        "/activities/Chess Club/unregister", params={"email": "notregistered@mergington.edu"}
    )

    assert response.status_code == 400
