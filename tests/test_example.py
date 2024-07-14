def test_read_example(test_app):
    response = test_app.get("/api/v1/example")
    assert response.status_code == 200
    assert response.json() == {"message": "This is an example endpoint"}
