from flask_marshmallow import Marshmallow


def create():
    ma = Marshmallow()
    return ma


serializer = create()
