from app.db import db


class AccountingModel(db.Document):
    """
    Модель БО.
    """
    inn = db.StringField(requirements=True, unique=True)
    data = db.DictField()
    period = db.StringField()
