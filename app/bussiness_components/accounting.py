from ..models import AccountingModel


class Accounting:
    """
    Класс БО.
    Взаимодействует с моделью.
    """

    def __init__(self, inn: str, data: dict):
        """
        inn - ИНН
        data - информация БО
        """
        self.inn = inn
        self.data = data

    def save(self):
        """
        Сохранить данные БО в БД.
        """
        AccountingModel(inn=self.inn, data=self.data).save()

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

    @staticmethod
    def exist(inn):
        """
        Проверить есть ли такое БО в БД
        """
        if AccountingModel.objects(inn=inn):
            return True
        return False
