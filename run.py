from app import create_app, settings
from app.config import Config

app = create_app(Config)

if __name__ == "__main__":
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )