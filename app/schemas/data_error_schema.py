from marshmallow import validate

from app import serializer
from .error_schema import ErrorSchema


class DataErrorSchema(serializer.Schema):
    """
    Схема данных с ошибкой
    """
    error = serializer.Nested(ErrorSchema())
    inn = serializer.String(validate=validate.Length(min=10, max=12))
