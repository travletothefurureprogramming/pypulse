
from app import create_app
import app.routes as routes


def test_root():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["status"] == "online"

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


def test_metrics_error(monkeypatch):
    def fake_cpu():
        raise RuntimeError("Secret internal error")

    def fake_ram():
        raise RuntimeError("Secret internal error")

    def fake_disk():
        raise RuntimeError("Secret internal error")

    def fake_boot_time():
        raise RuntimeError("Secret internal error")

    monkeypatch.setattr(routes, "cpu", fake_cpu)
    monkeypatch.setattr(routes, "ram", fake_ram)
    monkeypatch.setattr(routes, "disk", fake_disk)
    monkeypatch.setattr(routes, "system_boot_time", fake_boot_time)

    app = create_app()
    client = app.test_client()

    response = client.get("/api/metrics")

    assert response.status_code == 500
    assert response.json["status"] == "error"
    assert "Secret internal error" not in response.get_data(as_text=True)