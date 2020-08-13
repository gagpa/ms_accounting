from ..bussiness_components import NalogParserJson, Accounting, NalogValidatorInfo
from ..exceptions.invalid_app import InternalError
from ..exceptions.invalid_data import InvalidInn, InvalidOrgId, InvalidAccId


class AccountLogic:
    """
    Логика accounting view
    """

    def get_accounting(self, inn: str) -> dict:
        """
        Логика метода GET /accounting
        """
        try:
            NalogValidatorInfo.validate_inn(inn)
            if Accounting.exist(inn):
                collection = Accounting.get_object(inn)
                accounting = collection['data']
            else:
                parser = NalogParserJson()
                accounting = parser.parse_accounting(inn)
                collection = Accounting(inn, accounting)
                collection.save()
            return accounting
        except InvalidInn:
            raise InvalidInn
        except (InvalidOrgId, InvalidAccId):
            raise InternalError
