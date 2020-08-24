from ..bussiness_objects import ResponseDealer


class ErrorHandleLogic:

    def invalid_inn(self, error_message):
        """
        Логика обработчика ошибки InvalidInn.
        """
        error = {'code': 400,
                 'title': 'Передан неверный ИНН',
                 'detail': error_message}
        response = ResponseDealer.error(error=error)
        return response

    def page_not_found(self, error_message):
        """
        Логика обработчика ошибки не существующей страницы.
        """
        error = {'code': 404,
                 'title': 'Такой страницы не существует',
                 'detail': error_message
                 }
        response = ResponseDealer.error(error=error)
        return response

    def unexpected(self, error_message):
        """
        Логика обработки неожиданных ошибок.
        """
        error = {
            'code': 503,
            'title': 'Сервис временно не доступен',
            'detail': error_message
        }
        response = ResponseDealer.error(error=error)
        return response
