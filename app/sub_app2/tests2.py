def test_endpoint_with_var2(client):
    response = client.get("/items2/2")
    assert response.status_code == 200
    assert response.json() == {"item_id": 2}
