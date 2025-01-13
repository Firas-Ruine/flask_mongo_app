from .subscriber_routes import main as subscriber_routes
from .document_routes import main as document_routes
from .loan_routes import main as loan_routes

__all__ = ["subscriber_routes", "document_routes", "loan_routes"]
