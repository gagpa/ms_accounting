from app import serializer


class ErrorSchema(serializer.Schema):
    """
    Схема ошибки.
    """
    code = serializer.Integer()
    title = serializer.String()
    detail = serializer.String()
