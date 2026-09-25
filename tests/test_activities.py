def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data


def test_activity_entry_has_expected_fields(client):
    response = client.get("/activities")
    chess_club = response.json()["Chess Club"]

    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)
