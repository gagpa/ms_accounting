from app import serializer
from .error_schema import ErrorSchema


class ResponseErrorSchema(serializer.Schema):
    """
    Схема ответа с ошибкой
    """
    success = serializer.Boolean(default=False)
    error = serializer.Nested(ErrorSchema)
