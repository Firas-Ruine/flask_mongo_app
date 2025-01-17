from flask import Flask
from app.routes import subscriber_routes, document_routes, loan_routes, category_routes, dashboard_routes
from app.routes.html_routes import main as html_routes
from app.scheduler import start_scheduler

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(subscriber_routes, url_prefix='/api/subscribers')
    app.register_blueprint(document_routes, url_prefix='/api/documents')
    app.register_blueprint(loan_routes, url_prefix='/api/loans')
    app.register_blueprint(category_routes, url_prefix='/api/categories')
    app.register_blueprint(dashboard_routes, url_prefix='/api/dashboard')
    app.register_blueprint(html_routes)
    
    # Start scheduler
    start_scheduler()
    return app
