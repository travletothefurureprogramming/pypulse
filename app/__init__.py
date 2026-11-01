from flask import Flask, jsonify
import logging
from app.routes import main
from app.settings import LOG_FILE, LOG_LEVEL

def create_app(config_class=None):

    log_level = getattr(logging, LOG_LEVEL, None)

    if not isinstance(log_level, int):
        raise ValueError(f"Invalid logging level: {LOG_LEVEL}")

    logging.basicConfig(
        filename=LOG_FILE,
        level=log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        force=True
    )


    app = Flask(__name__)
    app.config.from_object(config_class or "app.config.Config")

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
    