from string import Template
import requests
import re


class ParserNalogJson:
    """
    Парсер.
    Занимается парсингом json объектов сайта https://bo.nalog.ru
    Парсит из JSON объектов:
     1) по ИНН, номер организации, присвоенный этим ресурсом;
     2) по номеру организации, номер БО, присвоенный этим ресурсомЖ;
     3) по номеру БО, БО.
    """

    __templates_url = {'search_org': Template('https://bo.nalog.ru/nbo/organizations/search?query=$inn')}
    __headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                               ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def get_request(self, link):
        """Сделать get запрос"""
        return requests.get(link, headers=self.__headers)

    @staticmethod
    def check_status_code(response):
        """
        Проверяет статусы код.
        Если код на 200, бросает исключения.
        """
        if response.status_code == 400:
            raise InvalidInn
        elif response.status_code == 403:
            raise InvalidHeadersRequest
        elif response.status_code != 200:
            raise ConnectionError
        else:
            return True

    def parse_organisation_id(self, inn: str) -> int:
        """Запарсить внутренний номер организации по ИНН"""
        if not inn:
            raise InvalidInn

        link = self.__templates_url['search_org'].substitute(inn=inn)
        response = self.get_request(link)
        self.check_status_code(response)
        response_data = response.json()['content']
        ValidatorNalogInfo.validate_inn(response_data, inn)
        org_id = response_data[0]['id']
        return org_id


class ValidatorNalogInfo:
    """Объект валидатор"""

    @staticmethod
    def validate_inn(data: list, expected_inn: str):
        """Проверить ИНН"""
        inn = data[0]['inn']
        inn = re.sub(r'[^0-9]*', '', inn)
        if len(data) != 1 or inn != expected_inn:
            raise InvalidInn


class InvalidHeadersRequest(ConnectionError):
    pass


class InvalidInn(ValueError):
    pass
