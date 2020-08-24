from pymongo.errors import ServerSelectionTimeoutError

from . import api
from ..bussiness_logics import ErrorHandleLogic
from ..exceptions.invalid_data import InvalidInn


@api.errorhandler(InvalidInn)
def error_invalid_inn(e):
    """
    Обработчкик ошибки неверно переданного ИНН.
    """
    response = ErrorHandleLogic().invalid_inn(repr(e))
    return response


@api.app_errorhandler(404)
def error_not_found(e):
    """
    Обработка 404 ошибки(страница не найдена).
    """
    response = ErrorHandleLogic().page_not_found(repr(e))
    return response


@api.errorhandler(ServerSelectionTimeoutError)
def error_db_off(e):
    """
    Обработка ошибки из-за невключенной БД.
    Сообщает, что к БД нет доступа.
    """
    return error_unexpected(e)


@api.errorhandler(Exception)
def error_unexpected(e):
    """
    Обработка неожиданных ошибок
    """
    response = ErrorHandleLogic().unexpected(repr(e))
    return response
