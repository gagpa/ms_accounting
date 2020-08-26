from datetime import datetime

from app import serializer
from .accounting_schema import AccountingSchema


class WebhookAccountingSchema(serializer.Schema):
    """
    Схема веб-хука с БО.
    """
    id = serializer.String()
    ms = serializer.String(default='accounting')
    event = serializer.String(default='success')
    time = serializer.String(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    data = serializer.Nested(AccountingSchema())
