
from app import create_app

def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "online"

def test_system():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/system")

    assert response.status_code == 200
    assert "hostname" in response.json
    assert "operating_system" in response.json
    assert "python_version" in response.json

def test_metrics():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/metrics")

    assert response.status_code == 200
    assert "cpu_percent" in response.json and response.json["cpu_percent"] >= 0 and response.json["cpu_percent"] <= 100
    assert "ram_percent" in response.json and response.json["ram_percent"] >= 0 and response.json["ram_percent"] <= 100
    assert "disk_percent" in response.json and response.json["disk_percent"] >= 0 and response.json["disk_percent"] <= 100
    assert "boot_time" in response.json and response.json["boot_time"] >= 0 


    