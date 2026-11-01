def test_list_posts_returns_200_and_100_items(session, base_url):
    r = session.get(f"{base_url}/posts")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) == 100


def test_single_post_schema(session, base_url):
    r = session.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    post = r.json()
    assert set(post.keys()) == {"userId", "id", "title", "body"}
    assert post["id"] == 1
    assert isinstance(post["title"], str) and post["title"]
    assert isinstance(post["body"], str) and post["body"]


def test_post_not_found_returns_404(session, base_url):
    r = session.get(f"{base_url}/posts/0")
    assert r.status_code == 404


def test_create_post_returns_201_and_echoes_body(session, base_url):
    payload = {"title": "teste", "body": "conteudo", "userId": 1}
    r = session.post(f"{base_url}/posts", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert created["userId"] == payload["userId"]
    assert "id" in created


def test_response_time_under_2_seconds(session, base_url):
    r = session.get(f"{base_url}/posts/1")
    assert r.elapsed.total_seconds() < 2.0
