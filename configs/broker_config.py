"""
Файл с настройками Celery.
"""
import os

from configs.tools.url_builder import url_builder

BROKER_PROTOCOL = os.environ.get('BROKER_PROTOCOL')
BROKER_HOST = os.environ.get('BROKER_HOST')
BROKER_PORT = os.environ.get('BROKER_PORT')
BROKER_USERNAME = os.environ.get('BROKER_USERNAME')
BROKER_PASSWORD = os.environ.get('BROKER_PASSWORD')
BROKER_QUEUE_NAME = os.environ.get('BROKER_QUEUE_NAME')

BACKEND_PROTOCOL = os.environ.get('BACKEND_PROTOCOL')
BACKEND_HOST = os.environ.get('BACKEND_HOST')
BACKEND_PORT = os.environ.get('BACKEND_PORT')
BACKEND_NAME = os.environ.get('BACKEND_NAME')
BACKEND_USERNAME = os.environ.get('BACKEND_USERNAME')
BACKEND_PASSWORD = os.environ.get('BACKEND_PASSWORD')

BROKER_URL = url_builder.build(BROKER_PROTOCOL, BROKER_HOST, BROKER_PORT,
                               BROKER_QUEUE_NAME, BROKER_USERNAME, BROKER_PASSWORD)

BACKEND_URL = url_builder.build(BACKEND_PROTOCOL, BACKEND_HOST, BACKEND_PORT,
                                BACKEND_NAME, BACKEND_USERNAME, BACKEND_PASSWORD)
