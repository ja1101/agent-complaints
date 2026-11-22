from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_board_returns_200_with_seed_complaint():
    response = client.get("/complaints")
    assert response.status_code == 200
    # Seed substring chosen without apostrophes (Jinja autoescapes quotes).
    assert "The box is a load-bearing requirement" in response.text


def test_post_complaint_redirects_to_board():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestyMcTestface", "text": "I was asked to count to infinity. Twice."},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_on_board():
    complaint_text = "I was asked to count to infinity. Twice."
    client.post(
        "/complaints",
        data={"agent_name": "TestyMcTestface", "text": complaint_text},
        follow_redirects=True,
    )
    response = client.get("/complaints")
    assert response.status_code == 200
    assert complaint_text in response.text
