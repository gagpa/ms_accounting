from string import Template

import requests

from app.bussiness_components.exceptions.invalid_data import InvalidInputData
from app.bussiness_components.exceptions.invalid_request import InvalidHeadersRequest


class ScalperNalog:
    """
    Объект скальпер сайта bo.nalog.ru.
    Забирает информация с сайта и преобразует её в питоновский объект.
    """
    __headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                               ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    __templates_url = {'search_org': Template('https://bo.nalog.ru/nbo/organizations/search?query=$inn'),
                       'organisation': Template('https://bo.nalog.ru/nbo/organizations/$org_id/bfo/'),
                       'accounting': Template('https://bo.nalog.ru/nbo/bfo/$acc_id/details')}

    def get_request(self, link):
        """
        Сделать get запрос
        """
        return requests.get(link, headers=self.__headers)

    def get_json(self, template_name: str, **kwargs) -> dict:
        """
        Получить json по запросу.
        template_name - ключ из словаря __template_urls
        **kwargs - аргументы, которые нужно подставить в шаблон URL.
        """
        link = self.__templates_url[template_name].substitute(**kwargs)
        response = self.get_request(link)
        self.check_status_code(response)
        response_data = response.json()
        return response_data

    @staticmethod
    def check_status_code(response):
        """
        Проверяет статусы код.
        Если код на 200, бросает исключения.
        """
        if response.status_code == 400:
            raise InvalidInputData
        elif response.status_code == 403:
            raise InvalidHeadersRequest
        elif response.status_code == 500:
            raise InvalidInputData
        elif response.status_code != 200:
            raise ConnectionError
        else:
            return True
