import logging
import platform
from datetime import UTC, datetime

from flask import Blueprint, jsonify

from app.monitor import cpu, disk, ram, system_boot_time

logger = logging.getLogger(__name__)

main = Blueprint("main", __name__)

@main.route("/health", methods=["GET"])
def system_health():
    try:
        return jsonify({
            "status": "online",
            "service": "PyPulse",
            "timestamp": datetime.now(UTC).isoformat()
        }), 200

    except Exception:
        logger.exception("Health check failed")
        return jsonify({
            "status": "error",
            "message": "Health check failed"
        }), 500

@main.route("/system", methods=["GET"])
def system_info():
    try:
        return jsonify({
            "hostname": platform.node(),
            "operating_system": platform.system(),
            "os_release": platform.release(),
            "python_version": platform.python_version()
        }), 200

    except Exception:
        logger.exception("Failed to retrieve system information")
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve system information"
        }), 500

@main.route("/metrics", methods=["GET"])
def metrics():
    try:
        return jsonify({
            "cpu_percent": cpu(),
            "ram_percent": ram(),
            "disk_percent": disk(),
            "boot_time": system_boot_time()
        }), 200

    except Exception:
        logger.exception("Failed to retrieve system metrics")
        return jsonify({
            "status": "error",
            "message": "Failed to retrieve system metrics"
        }), 500
