import os

from flask import Flask

from app.db import db
from app.queue import create_celery, init_celery
from app.serializer import serializer
from configs.main_config import main_config


def create_app(config_name):
    """
    Созадние объекта приложения.
    """
    app = Flask(__name__)
    config = main_config[config_name]
    app.config.from_object(config)
    init_celery(celery, app)
    db.init_app(app)
    serializer.init_app(app)

    from .api import api
    app.register_blueprint(blueprint=api, url_prefix='/api/v1')

    return app


celery = create_celery()
app = create_app(os.environ.get('APP_MODE') or 'default')
