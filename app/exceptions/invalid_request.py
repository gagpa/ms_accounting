"""
Файл с исключениями связанными с сетевыми запросами.
"""


class InvalidHeadersRequest(ConnectionError):
    """
    Заданы неправильные зоголовки у запроса.
    """
    error = {'code': 500,
             'title': 'Internal Error',
             'detail': 'Сервис недоступен'}


class PageNotFounded(ConnectionError):
    """
    Исключение страница не найдена.
    """
    error = {"code": 404,
             "title": "Not found",
             "detail": "Страница не существует"}
