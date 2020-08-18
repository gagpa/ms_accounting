from celery import Celery
from configs.celery_config import CeleryConfig


def create_celery():
    celery = Celery(__name__,
                    include=('app.tasks.nalog_parse_accounting',),
                    )
    celery.config_from_object(CeleryConfig)
    return celery


def init_celery(celery, app):
    celery.main = app.import_name
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
