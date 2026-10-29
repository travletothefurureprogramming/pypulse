from app import create_app, settings
from app.config import DevelopmentConfig, TestingConfig

app = create_app()
dev_app = create_app(DevelopmentConfig)
test_app = create_app(TestingConfig)

if __name__ == "__main__":
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )