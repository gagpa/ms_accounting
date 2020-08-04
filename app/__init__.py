from flask import Flask
import os


from configs.main_config import main_config


def create_app(config_name):
    """
    Созадние объекта приложения.
    """
    app = Flask(__name__)
    config = main_config[config_name]
    app.config.from_object(config)

    from .api import api
    app.register_blueprint(blueprint=api, url_prefix='/api/v1')

    return app


app = create_app(os.environ.get('APP_MODE') or 'default')
