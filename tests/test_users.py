def test_list_users_returns_10(session, base_url):
    r = session.get(f"{base_url}/users")
    assert r.status_code == 200
    assert len(r.json()) == 10


def test_user_schema(session, base_url):
    r = session.get(f"{base_url}/users/1")
    assert r.status_code == 200
    user = r.json()
    for field in ("id", "name", "username", "email", "address", "phone", "website", "company"):
        assert field in user
    assert "lat" in user["address"]["geo"]
    assert "lng" in user["address"]["geo"]


def test_user_albums_belong_to_user(session, base_url):
    r = session.get(f"{base_url}/users/1/albums")
    assert r.status_code == 200
    albums = r.json()
    assert len(albums) > 0
    assert all(a["userId"] == 1 for a in albums)
