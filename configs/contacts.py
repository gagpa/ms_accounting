"""
Файл с ссылками на сервисы.
"""
import os

contacts = \
    {
        'organisation': os.environ.get('WEBHOOK_URL'),
    }
