"""
Файл с исключениями связанные с не корректными данными
"""


class InvalidInputData(ValueError):
    """
    Переданы не корректные вводные данные.
    """
    pass


class InvalidOrgId(InvalidInputData):
    """
    Передан не корректный внутренний номер организации.
    """
    pass


class InvalidAccId(InvalidInputData):
    """
    Передан не корректный внутренний номер БО.
    """
    pass


class InvalidInn(InvalidInputData):
    """
    Передан не корректный ИНН.
    """
    pass
