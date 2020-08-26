"""
Файл с ошибками приложения
"""


class InternalError(Exception):
    """
    Исключение внутренней ошибки.
    """
    error = {'code': 500,
             'title': 'Internal Error',
             'detail': 'Сервис врменно не доступен'
             }
