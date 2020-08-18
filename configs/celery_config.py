import os


class CeleryConfig:
    """
    Класс кофигурации очереди задач Celery.
    """
    CELERY_BROKER_URL = os.environ.get('BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('RESULT_BACKEND')
