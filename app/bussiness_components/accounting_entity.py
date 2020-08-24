import json

from ..models import AccountingModel


class AccountingEntity:
    """
    Класс БО.
    Взаимодействует с моделью.
    """

    def __init__(self, inn: str, period: str, accounting: dict):
        """
        inn - ИНН
        data - информация БО
        """
        self.inn = inn
        self.period = period
        self.accounting = accounting

    def save(self):
        """
        Сохранить данные БО в БД.
        """
        AccountingModel(inn=self.inn, period=self.period, accounting=self.accounting).save()

    def delete(self):
        """
        Удалить данные БО в БД.
        """
        AccountingModel.objects(inn=self.inn).delete()

    @classmethod
    def get_object(cls, inn):
        """
        Получить из БД БО
        """
        collection = AccountingModel.objects(inn=inn).first()
        return collection

    @classmethod
    def get_dict(cls, inn):
        """
        Получить данные БО в формате dict.
        """
        collection = AccountingModel.objects(inn=inn).first()
        if collection:
            collection = json.loads(collection.to_json())
            collection.pop('_id')
        return collection

    @staticmethod
    def exist(inn):
        """
        Проверить есть ли такое БО в БД
        """
        if AccountingModel.objects(inn=inn):
            return True
        return False
