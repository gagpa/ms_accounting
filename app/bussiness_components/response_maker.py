from flask import make_response, jsonify
from app.exceptions import InvalidTypeResponse


class ResponseMaker:
    """
    Класс создатель ответов.
    Создаёт объект ответа для возврата его через View.
    """

    __STATUS = \
        {
            'create': 201,
            'success': 200
        }

    def make(self, json_dict: dict, type_response: str):
        """
        Создать объект ответа.
        """
        try:
            response = make_response(jsonify(json_dict), self.__STATUS[type_response])
            return response
        except KeyError:
            raise InvalidTypeResponse
