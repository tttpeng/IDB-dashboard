from flask import Flask
from app.models import db
from app import config

VERSION = (0, 2)

__version__ = ".".join(map(str, VERSION))
__status__ = "Alpha"
__description__ = "Simple blog system powered by Flask"
__author__ = "defshine"
__email__ = "crazyxin1988@gmail.com"
__license__ = "MIT License"


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    register_database(app)
    db.create_all()
    return app


def register_log():
    import logging
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)


def register_database(app):
    db.init_app(app)
    db.app = app






