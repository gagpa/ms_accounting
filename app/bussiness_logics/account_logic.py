from ..bussiness_components import NalogParserJson


class AccountLogic:
    """
    Логика accounting view
    """

    def get_accounting(self, inn: str) -> dict:
        """
        Логика метода GET /accounting
        """
        parser = NalogParserJson()
        accounting = parser.parse_accounting(inn)
        return accounting
