from flask import jsonify

from . import api
from ..exceptions.invalid_data import InvalidInn
from pymongo.errors import ServerSelectionTimeoutError


@api.errorhandler(InvalidInn)
def error_invalid_inn(e):
    """
    Обработчкик ошибки неверно переданного ИНН.
    """
    status_code = 400
    return jsonify(
        {
            'success': False,
            'message': 'Не верный ИНН'
        }
    ), status_code


@api.app_errorhandler(404)
def error_not_found(e):
    """
    Обработка 404 ошибки(страница не найдена).
    """
    status_code = 404
    return jsonify({
        'success': False,
        'message': 'Такой страницы не существует.'
    }), status_code


@api.errorhandler(ServerSelectionTimeoutError)
def error_db_off(e):
    """
    Обработка ошибки из-за невключенной БД.
    Сообщает, что к БД нет доступа.
    """
    return error_unexpected(e)


# @api.errorhandler(Exception)
# def error_unexpected(e):
#     """
#     Обработка неожиданных ошибок
#     """
#     status_code = 503
#     return jsonify({
#             'success': False,
#             'message': 'Сервис не доступен'
#         }), status_code
