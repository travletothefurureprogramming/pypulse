from flask import Flask
from app.routes import main, jsonify

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main, url_prefix="/api")

    @app.get("/")
    def root():
        return jsonify({
            "service": "PyPulse",
            "message": "System Monitoring API",
            "status": "online",
            "endpoints": {
                "health": "/api/health",
                "system": "/api/system",
                "metrics": "/api/metrics"
            }
        }), 200

    return app
    