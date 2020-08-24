from celery import current_app as app

from app.decorators import organisation_webhook
from ..bussiness_components import NalogParserJson, AccountingEntity, NalogValidatorInfo


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
        accounting_dict = AccountingEntity.get_dict(self.inn)
        return accounting_dict

    def parse(self) -> dict:
        """
        Запарсить БО с сайта bo.nalog.ru.
        """
        parser = NalogParserJson()
        accounting = parser.parse_accounting(self.inn)
        period = parser.parse_period_accounting(self.inn)
        AccountingEntity(self.inn, period, accounting).save()
        accounting_dict = AccountingEntity.get_dict(self.inn)
        return accounting_dict

    def task_parse(self):
        task_parse.delay(self.inn)


@app.task(name='parse.accounting')
@organisation_webhook
def task_parse(inn, ) -> dict:
    """
    Поставить задачу в очередь.
    Сделаить метод parse().
    """
    ag = AccountingGetter(inn)
    accounting_dict = ag.parse()
    return accounting_dict
