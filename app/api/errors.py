from pymongo.errors import ServerSelectionTimeoutError

from . import api
from ..bussiness_logics import ErrorHandleLogic
from ..exceptions import InvalidInn, UnregisteredInn, PageNotFounded, InternalError


@api.errorhandler(InvalidInn)
def error_invalid_inn(e):
    """
    Обработчкик ошибки неверно переданного ИНН.
    """
    response = ErrorHandleLogic().response(e)
    return response


@api.errorhandler(UnregisteredInn)
def error_unregistered_inn(e):
    """
    Обработчик ошибки незарегестрированного ИНН.
    """
    response = ErrorHandleLogic().response(e)
    return response


@api.app_errorhandler(404)
def error_not_found(e):
    """
    Обработка 404 ошибки(страница не найдена).
    """
    e = PageNotFounded
    response = ErrorHandleLogic().response(e)
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
    e = InternalError
    response = ErrorHandleLogic().response(e)
    return response
