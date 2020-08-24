from configs.contacts import contacts
import requests


class Requester:
    """
    Класс, посылающий запрос.
    Может сделать веб-хук.
    """
    __contacts = contacts

    def _is_success(self, response) -> bool:
        """
        Проверить успешный код или нет.
        """
        return response.status_code == 200

    def webhook(self, contact_name, **kwargs) -> bool:
        """
        Послать веб-хук на contact_url.
        """
        contact_url = self.__contacts[contact_name]
        response = self.get_request(contact_url, **kwargs)
        return self.is_success(response)

    def get_request(self, contact_url, **kwargs):
        """
        Сделать GET запрос на contact_url.
        """
        response = requests.get(contact_url, json=kwargs['json'])
        return response
