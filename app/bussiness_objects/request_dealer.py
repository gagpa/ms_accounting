from configs.contacts import contacts
from ..bussiness_components import Requester
from ..schemas import WebhookErrorSchema, WebhookAccountingSchema


class RequestDealer:
    """
    Класс делающий конкретные запросы
    """

    __contacts = contacts

    def __init__(self, contact):
        self.contact_url = self.__contacts[contact]
        self.requester = Requester()

    def send_accounting_webhook(self, accounting: dict, **kwargs):
        """
        Отправить веб-хук с БО.
        """
        data = {
            'data': accounting
        }
        json_message = WebhookAccountingSchema().dump(data)
        response = self.requester.get_request(self.contact_url, json=json_message, **kwargs)
        success = self.requester.is_success(response)
        return success

    def send_error_webhook(self, inn, error: dict, **kwargs):
        """
        Отправить веб-хук с ошибкой.
        """
        data = {
            'data':
                {
                    'inn': inn,
                    'error': error
                }
        }
        json_message = WebhookErrorSchema().dump(data)
        response = self.requester.get_request(self.contact_url, json=json_message, **kwargs)
        success = self.requester.is_success(response)
        return success
