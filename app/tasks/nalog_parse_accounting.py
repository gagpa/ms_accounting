from app import celery
from app.bussiness_components import Accounting, NalogParserJson


@celery.task(name='parser.accounting')
def parse_accounting(inn):
    """
    Задачи в очереди. Парсить БО с сайта bo.nalog.ru
    """
    parser = NalogParserJson()
    accounting = parser.parse_accounting(inn)
    Accounting(inn, accounting).save()
    return accounting
