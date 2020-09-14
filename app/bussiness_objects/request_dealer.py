from ..bussiness_components import Requester
from ..schemas import WebhookErrorSchema, WebhookAccountingSchema


class RequestDealer:
    """
    Класс делающий конкретные запросы
    """

    def __init__(self):
        self.requester = Requester()

    def send_accounting_webhook(self, url: str, accounting: dict, **kwargs):
        """
        Отправить веб-хук с БО.
        """
        data = \
            {
                'data': accounting
            }
        json_message = WebhookAccountingSchema().dump(data)
        response = self.requester.get_request(url, json=json_message, **kwargs)
        success = self.requester.is_success(response)
        return success

    def send_error_webhook(self, url, inn, error: dict, **kwargs):
        """
        Отправить веб-хук с ошибкой.
        """
        data = \
            {
                'data':
                    {
                        'inn': inn,
                        'error': error
                    }
            }
        json_message = WebhookErrorSchema().dump(data)
        response = self.requester.get_request(url, json=json_message, **kwargs)
        success = self.requester.is_success(response)
        return success
