from flask import Flask, jsonify
import logging
from app.routes import main

def create_app():

    logging.basicConfig(
        filename="pypulse.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        force=True
    )

    app = Flask(__name__)

    app.register_blueprint(main, url_prefix="/api")

    logging.info("PyPulse application created")    
    
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
    