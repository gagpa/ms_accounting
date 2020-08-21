from app.schemas.response_in_queue import ResponseInQueue
from flask import make_response, jsonify


class ResponseDealer:

    @staticmethod
    def in_queue(**kwargs):
        """
        Подготовить ответ от сервера, что клиента поставили в очередь
        """
        response_json = ResponseInQueue().dump({})
        status = 201
        response = make_response(jsonify(response_json), status)
        return response
