import re

from .exceptions.invalid_data import InvalidInn, InvalidOrgId


class NalogValidatorInfo:
    """
    Объект валидатор данных, которые используются или парсятся с сайта bo.nalog.ru.
    """

    @staticmethod
    def validate_parse_inn(parse_inn: str, expected_inn: str):
        """
        Проверить ИНН.
        """
        if not isinstance(parse_inn, str):
            raise InvalidInn
        inn = re.sub(r'[^\-0-9]*', '', parse_inn)
        NalogValidatorInfo.validate_inn(inn)
        if inn != expected_inn:
            raise InvalidInn

    @staticmethod
    def validate_inn(inn: str):
        """
        Проверить число, что оно может быть ИНН.
        """
        if not isinstance(inn, str) or not inn.isdigit() or len(inn) not in (10, 12):
            raise InvalidInn

    @staticmethod
    def validate_organisation_json(json: list):
        """
        Проверить json организации на валидность.
        """
        if not json and isinstance(json, list):
            raise InvalidOrgId
