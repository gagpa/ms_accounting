from app import serializer


class ResponseInQueue(serializer.Schema):
    success = serializer.Boolean(default=True)
