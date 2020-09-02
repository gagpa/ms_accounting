"""
Файл с исключениями связанные с не корректными данными
"""


class InvalidInputData(ValueError):
    """
    Переданы не корректные вводные данные.
    """
    error = {'code': 503,
             'title': 'Internal Error',
             'detail': 'Сервис недоступен'
             }


class InvalidOrgId(InvalidInputData):
    """
    Передан не корректный внутренний номер организации.
    """
    error = {'code': 503,
             'title': 'Internal Error',
             'detail': 'Сервис недоступен'
             }


class InvalidAccId(InvalidInputData):
    """
    Передан не корректный внутренний номер БО.
    """
    error = {'code': 500,
             'title': 'Internal Error',
             'detail': 'Сервис недоступен'}


class InvalidInn(InvalidInputData):
    """
    Передан не корректный ИНН.
    """
    error = {'code': 422,
             'title': 'Validation Error',
             'detail': 'Передан неверный ИНН'}


class UnregisteredInn(InvalidInn):
    """
    Передан не зарегестрированный ИНН.
    """

    error = {'code': 422,
             'title': 'Validation Error',
             'detail': 'Переданный ИНН незарегистрирован в базе'}
