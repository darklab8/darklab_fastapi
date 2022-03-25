def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_endpoint_with_var(client):
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json() == {"item_id": 2}
