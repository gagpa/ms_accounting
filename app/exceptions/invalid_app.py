"""
Файл с ошибками приложения
"""


class InternalError(Exception):
    """
    Исключение внутренней ошибки.
    """
    error = {'code': 500,
             'title': 'Internal Error',
             'detail': 'Сервис временно недоступен'
             }


class InvalidToken(Exception):
    """
    Исключение неверный токен.
    """
    error = {'code': 401,
             'title': 'Validation Error',
             'detail': 'Передан неверный токен'
             }
