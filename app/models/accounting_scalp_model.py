from app.db import db


class AccountingScalpModel(db.Document):
    """
    Модель БО.
    """
    inn = db.StringField(requirements=True, unique=True)
    accounting = db.DictField()
    period = db.StringField()
    parse_date = db.DateTimeField()
