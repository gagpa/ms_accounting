import re

from .exceptions.invalid_data import InvalidInn, InvalidOrgId


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
