"""
Файл с настройками базы данных.
"""
import os

from configs.tools.url_builder import url_builder

DB_PROTOCOL = 'mongodb'

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))
DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

DB_URL = url_builder.build(DB_PROTOCOL, DB_HOST, DB_PORT, DB_NAME, DB_USERNAME, DB_PASSWORD)

MONGODB_SETTINGS = \
    {
        'db': DB_NAME,
        'host': DB_URL,
        'port': DB_PORT,
        'username': DB_USERNAME,
        'password': DB_PASSWORD,
    }
