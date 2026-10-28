from flask import Blueprint, jsonify
from datetime import datetime, timezone
from app.monitor import cpu, ram, disk, system_boot_time
import platform

main = Blueprint("main", __name__)

@main.route("/health", methods=["GET"])
def system_health():
    return jsonify({
        "status": "online",
        "service": "PyPulse",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200

@main.route("/system", methods=["GET"])
def system_info():
    return jsonify({
        "hostname": platform.node(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "python_version": platform.python_version()
    }), 200

@main.route("/metrics", methods=["GET"])
def metrics():
    return jsonify({
        "cpu_percent": cpu(),
        "ram_percent": ram(),
        "disk_percent": disk(),
        "boot_time": system_boot_time()
    }), 200
