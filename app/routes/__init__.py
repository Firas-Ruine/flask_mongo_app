# Import all blueprints
from .data_routes import main as data_routes
from .healthcheck import main as healthcheck

# Expose the blueprints for easy access
__all__ = ["data_routes", "healthcheck"]
