"""AI Doc Generator"""
__version__ = "0.1.0"
from .core.generator import DocumentationGenerator
from .core.config import Config
__all__ = ["DocumentationGenerator", "Config"]
