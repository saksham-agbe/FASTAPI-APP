class TestHealthAPI:

    def test_health_check(self, client):
        response = client.get("/api/Healthcheck")
        assert response.status_code == 200
    
    def test_health_check_content(self, client):
        response = client.get("/api/Healthcheck")
        data = response.json()
        assert "success" in data
        assert data["success"] is True
        assert "message" in data
