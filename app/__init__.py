from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import data_routes, mongo_check
    app.register_blueprint(data_routes)
    app.register_blueprint(mongo_check)

    return app
