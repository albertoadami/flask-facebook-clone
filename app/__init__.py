from flask import Flask
from app.routes import health
import logging

def create_app():
    app = Flask(__name__)
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)

    # Register blueprints
    app.register_blueprint(health.bp)
    return app
