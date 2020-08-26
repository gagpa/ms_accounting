import requests


class Requester:
    """
    Класс, посылающий запрос.
    Может сделать веб-хук.
    """

    def is_success(self, response) -> bool:
        """
        Проверить успешный код или нет.
        """
        return response.status_code == 200

    def get_request(self, contact_url, **kwargs):
        """
        Сделать GET запрос на contact_url.
        """
        response = requests.get(contact_url, json=kwargs['json'])
        return response
