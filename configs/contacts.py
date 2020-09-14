"""
Файл с ссылками на сервисы.
"""
import os

contacts = \
    {
        os.environ.get('AUTH_TOKEN'): os.environ.get('WEBHOOK_URL'),
    }
