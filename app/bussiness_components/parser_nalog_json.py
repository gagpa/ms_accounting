from json import JSONDecodeError
from string import Template

import requests

from app.bussiness_components.exceptions.invalid_data import InvalidInn, InvalidAccId, InvalidInputData, InvalidOrgId
from app.bussiness_components.exceptions.invalid_request import InvalidHeadersRequest
from .validator_nalog_info import ValidatorNalogInfo


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

    def parse_organisation_id(self, inn: str) -> str:
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
        org_id = str(content[0]['id'])
        return org_id

    def parse_accounting_id(self, organisation_id: str) -> str:
        """
        Запарсить внутренний номер БО по врнутреннему номеру организации
        """
        try:
            response_data = self.get_json('organisation', org_id=organisation_id)
        except (InvalidInputData, JSONDecodeError):
            raise InvalidOrgId
        ValidatorNalogInfo.validate_organisation_json(response_data)
        acc_id = str(response_data[0]['id'])
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
        org_id = self.parse_organisation_id(inn)
        acc_id = self.parse_accounting_id(org_id)
        accounting = self.parse_accounting_json(acc_id)
        return accounting
