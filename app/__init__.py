from flask import Flask
from app.routes import health

def create_app():
    app = Flask(__name__)
    # Register blueprints
    app.register_blueprint(health.bp)
    return app
