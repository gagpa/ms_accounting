from ..bussiness_components import NalogParserJson
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
            parser = NalogParserJson()
            accounting = parser.parse_accounting(inn)
            return accounting
        except InvalidInn:
            raise InvalidInn
        except (InvalidOrgId, InvalidAccId):
            raise InternalError
