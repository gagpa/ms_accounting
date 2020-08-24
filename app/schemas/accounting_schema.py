from marshmallow import validate

from app import serializer
from .custome_fields.accounting_data_field import AccountingDataField


class AccountingSchema(serializer.Schema):
    """
    Схема БО.
    """
    inn = serializer.String(validate=validate.Length(min=10, max=12))
    period = serializer.String(load_only=True)
    accounting = AccountingDataField()
