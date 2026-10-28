from flask import Blueprint, jsonify
from datetime import datetime, timezone
import platform

main = Blueprint("main", __name__)

@main.route("/helath", methods=["GET"])
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
