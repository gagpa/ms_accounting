from app import serializer


class ResponseInQueueSchema(serializer.Schema):
    success = serializer.Boolean(default=True)
