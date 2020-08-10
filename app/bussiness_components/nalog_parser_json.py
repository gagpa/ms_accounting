from json import JSONDecodeError

from app.bussiness_components.exceptions.invalid_data import InvalidInn, InvalidAccId, InvalidInputData, InvalidOrgId
from .nalog_scalper import NalogScalper
from .nalog_validator_info import NalogValidatorInfo


class NalogParserJson:
    """
    Парсер.
    Занимается парсингом json объектов сайта https://bo.nalog.ru
    Парсит из JSON объектов:
     1) по ИНН, номер организации, присвоенный этим ресурсом;
     2) по номеру организации, номер БО, присвоенный этим ресурсомЖ;
     3) по номеру БО, БО.
    """

    def __init__(self):
        self.scalp = NalogScalper()
        self.validator = NalogValidatorInfo()

    def parse_organisation_id(self, inn: str) -> str:
        """
        Запарсить внутренний номер организации по ИНН
        """
        self.validator.validate_inn(inn)
        try:
            response_data = self.scalp.get_json('search_org', inn=inn)
        except (InvalidInputData, JSONDecodeError):
            raise InvalidInn
        content = response_data['content']
        parse_inn = content[0]['inn']
        self.validator.validate_parse_inn(parse_inn, inn)
        org_id = str(content[0]['id'])
        return org_id

    def parse_accounting_id(self, organisation_id: str) -> str:
        """
        Запарсить внутренний номер БО по врнутреннему номеру организации
        """
        try:
            response_data = self.scalp.get_json('organisation', org_id=organisation_id)
        except (InvalidInputData, JSONDecodeError):
            raise InvalidOrgId
        self.validator.validate_organisation_json(response_data)
        acc_id = str(response_data[0]['id'])
        return acc_id

    def parse_accounting_json(self, accounting_id: str) -> dict:
        """
        Запарсить БО по внутреннему номеру БО.
        """
        try:
            response_data = self.scalp.get_json('accounting', acc_id=accounting_id)
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
