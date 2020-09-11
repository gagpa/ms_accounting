import json

from ..models import AccountingScalpModel
from datetime import datetime


class AccountingScalpEntity:
    """
    Класс для взаимодействия с моделью AccountingScalpModel.
    """

    def __init__(self, inn: str, period: str, accounting: dict, parse_date=None):
        """
        inn - ИНН
        period - периоды БО
        data - информация БО
        parse_date - время получения информации от источника
        """
        self.inn = inn
        self.period = period
        self.accounting = accounting
        self.parse_date = parse_date or datetime.now()

    def save(self):
        """
        Сохранить данные БО в БД.
        """
        AccountingScalpModel(inn=self.inn,
                             period=self.period,
                             accounting=self.accounting,
                             parse_date=self.parse_date).save()

    def delete(self):
        """
        Удалить данные БО в БД.
        """
        AccountingScalpModel.objects(inn=self.inn).delete()

    @classmethod
    def get_object(cls, inn):
        """
        Получить из БД БО
        """
        collection = AccountingScalpModel.objects(inn=inn).first()
        return collection

    @classmethod
    def get_dict(cls, inn):
        """
        Получить данные БО в формате dict.
        """
        collection = AccountingScalpModel.objects(inn=inn).first()
        if collection:
            collection = json.loads(collection.to_json())
            collection.pop('_id')
        return collection

    @staticmethod
    def exist(inn):
        """
        Проверить есть ли такое БО в БД
        """
        if AccountingScalpModel.objects(inn=inn):
            return True
        return False
