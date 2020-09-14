from celery import current_app as app
from mongoengine.errors import NotUniqueError
from app.exceptions import InvalidInn, UnregisteredInn, InternalError
from configs.task_config import QUEUE_COUNTDOWN
from ..bussiness_components import NalogParserJson, AccountingScalpEntity, NalogValidatorInfo
from ..bussiness_objects.request_dealer import RequestDealer


class AccountingGetter:
    """
    Класс владеющий всеми методами достать полноценный БО.
    """

    def __init__(self, inn: str):
        NalogValidatorInfo.validate_inn(inn)
        self.inn = inn

    def from_db(self):
        """
        Достать БО из БД.
        """
        accounting_dict = AccountingScalpEntity.get_dict(self.inn)
        return accounting_dict

    def parse(self) -> dict:
        """
        Запарсить БО с сайта bo.nalog.ru.
        """
        parser = NalogParserJson()
        accounting = parser.parse_accounting(self.inn)
        period = parser.parse_period_accounting(self.inn)
        AccountingScalpEntity(self.inn, period, accounting).save()
        accounting_dict = AccountingScalpEntity.get_dict(self.inn)
        return accounting_dict

    def task_parse(self):
        task_parse.apply_async((self.inn,), countdown=int(QUEUE_COUNTDOWN))


@app.task(name='parse.accounting')
def task_parse(inn) -> dict:
    """
    Поставить задачу в очередь.
    Вызвать метод parse и отправить результат с помощью веб-хука.
    """
    requester = RequestDealer('organisation')
    try:
        ag = AccountingGetter(inn)
        try:
            accounting_dict = ag.parse()
        except NotUniqueError:
            accounting_dict = ag.from_db()
        requester.send_accounting_webhook(accounting_dict)
        return accounting_dict

    except UnregisteredInn as e:
        requester.send_error_webhook(inn, e.error)
    except InvalidInn as e:
        requester.send_error_webhook(inn, e.error)
    except Exception:
        e = InternalError
        requester.send_error_webhook(inn, e.error)
