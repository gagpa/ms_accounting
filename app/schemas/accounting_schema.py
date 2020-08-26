from marshmallow import validate

from app import serializer
from .custome_fields import AccountingDataField, PeriodsField


class AccountingSchema(serializer.Schema):
    """
    Схема БО.
    """
    inn = serializer.String(validate=validate.Length(min=10, max=12))
    period = serializer.String(load_only=True)
    accounting = AccountingDataField()
    years = PeriodsField(default=None)
