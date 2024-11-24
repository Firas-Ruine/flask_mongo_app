# Import all blueprints
from .data_routes import main as data_routes
from .mongo_check import main as mongo_check

# Expose the blueprints for easy access
__all__ = ["data_routes", "mongo_check"]
