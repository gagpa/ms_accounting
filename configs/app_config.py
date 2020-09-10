from .broker_config import BROKER_URL, BACKEND_URL
from .db_config import MONGODB_SETTINGS


class Config:
    """
    Супер класс настроек приложения.
    """
    MONGODB_SETTINGS = MONGODB_SETTINGS
    CELERY_BROKER_URL = BROKER_URL
    CELERY_RESULT_BACKEND = BACKEND_URL

    @classmethod
    def init_app(cls, app):
        app.config.from_object(cls)


class DevelopmentConfig(Config):
    """
    Класс настроек для разработчика.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Класс настроек в production
    """
    pass


app_config = \
    {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
    }
