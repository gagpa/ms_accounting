from app.schemas import ResponseInQueueSchema, ResponseAccountingSchema, ResponseErrorSchema
from ..bussiness_components import ResponseMaker


class ResponseDealer:
    """
    Класс дилер ответов от сервера.
    Может дать ответы:
    1) задача в очереди;
    2) БО;
    3) об ошибке.
    """

    def __init__(self):
        self.responser = ResponseMaker()

    def in_queue(self, **kwargs):
        """
        Подготовить ответ от сервера, что клиента поставили в очередь
        """
        response_dict = ResponseInQueueSchema().dump({})
        type_response = 'success'
        response = self.responser.make(response_dict, type_response)
        return response

    def accounting(self, **kwargs):
        """
        Подготовить ответ от сервера с инорфмацией БО.
        """
        response_dict = ResponseAccountingSchema().dump({'data': kwargs['data']})
        type_response = 'create'
        response = self.responser.make(response_dict, type_response)
        return response

    def error(self, **kwargs):
        """
        Подготовить ответ от сервера с информацией БО
        """
        response_dict = ResponseErrorSchema().dump({'error': kwargs['error']})
        type_response = 'success'
        response = self.responser.make(response_dict, type_response)
        return response
