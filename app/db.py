"""
Файл с созданием db
"""
from flask_mongoengine import MongoEngine


def create_db():
    """
    Функция создания объекта db
    """
    mongo_db = MongoEngine()
    return mongo_db


db = create_db()
