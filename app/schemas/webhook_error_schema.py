from datetime import datetime

from app import serializer
from .data_error_schema import DataErrorSchema


class WebhookErrorSchema(serializer.Schema):
    """
    Схема веб-хука с ошибкой.
    """
    id = serializer.String()
    ms = serializer.String(default='accounting')
    event = serializer.String(default='error')
    time = serializer.String(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    data = serializer.Nested(DataErrorSchema())
