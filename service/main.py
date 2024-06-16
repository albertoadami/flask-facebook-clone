from flask import Flask
from .routes import health


app = Flask(__name__)

# Register blueprints
app.register_blueprint(health.bp)

if __name__ == "__main__":
    app.run(debug=True)
