"""
Файл с исключениями связанными с сетевыми запросами.
"""


class InvalidHeadersRequest(ConnectionError):
    """
    Заданы неправильные зоголовки у запроса.
    """
    pass
