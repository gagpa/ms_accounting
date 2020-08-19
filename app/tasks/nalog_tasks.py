from app import celery
from app.bussiness_components import Accounting, NalogParserJson
from app.decorators.organisation_webhook import organisation_webhook


@celery.task(name='get.accounting')
@organisation_webhook
def task_get_accounting(inn):
    """
    Задачи в очереди. Парсить БО с сайта bo.nalog.ru
    """
    parser = NalogParserJson()
    accounting = parser.parse_accounting(inn)
    Accounting(inn, accounting).save()
    return accounting
