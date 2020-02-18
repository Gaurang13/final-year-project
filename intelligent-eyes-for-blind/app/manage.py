from flask import Flask
from .config import configure_app
__all__ = ['create_app']


def create_app():
    """Initialize Flask Application"""

    app = Flask(__name__)
    configure_app(app)
    return app
