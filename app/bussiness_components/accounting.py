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
