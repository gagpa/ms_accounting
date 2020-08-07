from string import Template
import requests
import re
from json import JSONDecodeError


class ParserNalogJson:
    """
    Парсер.
    Занимается парсингом json объектов сайта https://bo.nalog.ru
    Парсит из JSON объектов:
     1) по ИНН, номер организации, присвоенный этим ресурсом;
     2) по номеру организации, номер БО, присвоенный этим ресурсомЖ;
     3) по номеру БО, БО.
    """

    __templates_url = {'search_org': Template('https://bo.nalog.ru/nbo/organizations/search?query=$inn'),
                       'organisation': Template('https://bo.nalog.ru/nbo/organizations/$org_id/bfo/'),
                       'accounting': Template('https://bo.nalog.ru/nbo/bfo/$acc_id/details')}
    __headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                               ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def get_request(self, link):
        """
        Сделать get запрос
        """
        return requests.get(link, headers=self.__headers)

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

    def parse_organisation_id(self, inn: str) -> int:
        """
        Запарсить внутренний номер организации по ИНН
        """
        if not inn:
            raise InvalidInn
        try:
            response_data = self.get_json('search_org', inn=inn)
        except (InvalidInputData, JSONDecodeError):
            raise InvalidOrgId
        content = response_data['content']
        ValidatorNalogInfo.validate_inn(content, inn)
        org_id = content[0]['id']
        return org_id

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

    def parse_accounting_id(self, organisation_id: str) -> int:
        """
        Запарсить внутренний номер БО по врнутреннему номеру организации
        """
        try:
            response_data = self.get_json('organisation', org_id=organisation_id)
        except (InvalidInputData, JSONDecodeError):
            raise InvalidOrgId
        ValidatorNalogInfo.validate_organisation_json(response_data)
        acc_id = response_data[0]['id']
        return acc_id

    def parse_accounting_json(self, accounting_id: str) -> dict:
        """
        Запарсить БО по внутреннему номеру БО.
        """
        try:
            response_data = self.get_json('accounting', acc_id=accounting_id)
        except (InvalidInputData, JSONDecodeError):
            raise InvalidAccId
        accounting = response_data
        return accounting

    def parse_accounting(self, inn: str) -> dict:
        """
        Запарсить БО по ИНН организации
        """
        org_id = str(self.parse_organisation_id(inn))
        acc_id = str(self.parse_accounting_id(org_id))
        accounting = self.parse_accounting_json(acc_id)
        return accounting


class ValidatorNalogInfo:
    """
    Объект валидатор.
    """

    @staticmethod
    def validate_inn(data: list, expected_inn: str):
        """
        Проверить ИНН.
        """
        inn = data[0]['inn']
        inn = re.sub(r'[^0-9]*', '', inn)
        if len(data) != 1 or inn != expected_inn:
            raise InvalidInn

    @staticmethod
    def validate_org_id(org_id: str):
        """
        Проверить внутренний номер организации.
        """
        if not isinstance(org_id, str) or not org_id:
            raise InvalidOrgId

    @staticmethod
    def validate_organisation_json(json):
        """
        Проверить json организации на валидность.
        """
        if not json:
            raise InvalidOrgId


class InvalidHeadersRequest(ConnectionError):
    """
    Заданы неправильные зоголовки у запроса.
    """
    pass


class InvalidInputData(ValueError):
    """
    Переданы не корректные вводные данные.
    """
    pass


class InvalidOrgId(InvalidInputData):
    """
    Передан не корректный внутренний номер организации.
    """
    pass


class InvalidAccId(InvalidInputData):
    """
    Передан не корректный внутренний номер БО.
    """
    pass


class InvalidInn(InvalidInputData):
    """
    Передан не корректный ИНН.
    """
    pass
