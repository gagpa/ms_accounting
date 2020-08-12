from ..models import AccountingModel


class Accounting:
    """
    Класс БО
    """

    def __init__(self, inn: str, data: dict):
        self.inn = inn
        self.data = data

    def save(self):
        AccountingModel(self.inn, self.data).save()
