import os

from flask import Flask

from app.db import db
# from app.queue import create_celery, init_celery
from app.queue import make_celery
from app.serializer import serializer
from configs.app_config import app_config


def create_app(config_name):
    """
    Созадние объекта приложения.
    """
    app = Flask(__name__)
    config = app_config[config_name]
    config.init_app(app)
    app.config.from_object(config)
    make_celery(app)
    # init_celery(celery, app)
    db.init_app(app)
    serializer.init_app(app)

    from .api import api
    app.register_blueprint(blueprint=api, url_prefix='/api/v1')

    return app


# celery = create_celery()
app = create_app(os.environ.get('APP_MODE') or 'default')
