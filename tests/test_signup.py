def test_signup_success(client):
    response = client.post(
        "/activities/Chess Club/signup", params={"email": "newstudent@mergington.edu"}
    )

    assert response.status_code == 200
    assert "newstudent@mergington.edu" in client.get("/activities").json()["Chess Club"]["participants"]


def test_signup_unknown_activity_returns_404(client):
    response = client.post(
        "/activities/Unknown Club/signup", params={"email": "newstudent@mergington.edu"}
    )

    assert response.status_code == 404


def test_signup_duplicate_returns_400(client):
    response = client.post(
        "/activities/Chess Club/signup", params={"email": "michael@mergington.edu"}
    )

    assert response.status_code == 400
