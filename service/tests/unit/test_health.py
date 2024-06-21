# tests/test_health.py
def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 204
    assert response.data == ""