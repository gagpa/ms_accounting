from ..bussiness_objects import ResponseDealer


class ErrorHandleLogic:
    """
    Класс логики обработки ошибок.
    """

    def response(self, exception):
        response = ResponseDealer.error(error=exception.error)
        return response
