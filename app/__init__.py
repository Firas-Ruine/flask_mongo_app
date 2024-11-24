from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    from .routes import data_routes, healthcheck
    app.register_blueprint(data_routes, url_prefix="/api/data")
    app.register_blueprint(healthcheck, url_prefix="/api/health")

    return app
