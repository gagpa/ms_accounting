from flask import make_response, jsonify

from app.schemas import ResponseInQueueSchema, ResponseAccountingSchema, ResponseErrorSchema


class ResponseDealer:
    """
    Класс дилер ответов от сервера.
    """

    @staticmethod
    def in_queue(**kwargs):
        """
        Подготовить ответ от сервера, что клиента поставили в очередь
        """
        response_dict = ResponseInQueueSchema().dump({})
        status = 201
        response = make_response(jsonify(response_dict), status)
        return response

    @staticmethod
    def accounting(**kwargs):
        """
        Подготовить ответ от сервера с инорфмацией БО.
        """
        response_dict = ResponseAccountingSchema().dump({'data': kwargs['data']})
        status = 200
        response = make_response(jsonify(response_dict), status)
        return response

    @staticmethod
    def error(**kwargs):
        """
        Подготовить ответ от сервера с информацией БО
        """
        response_dict = ResponseErrorSchema().dump({'error': kwargs['error']})
        status = 200
        response = make_response(jsonify(response_dict), status)
        return response
