from app import serializer
from .accounting_schema import AccountingSchema


class ResponseAccountingSchema(serializer.Schema):
    """
    Схема ответа с БО.
    """
    success = serializer.Boolean(default=True)
    data = serializer.Nested(AccountingSchema)
