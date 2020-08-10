from ..bussiness_components.parser_nalog_json import ParserNalogJson


class AccountLogic:
    """
    Логика accounting view
    """

    def get_accounting(self, inn: str) -> dict:
        """
        Логика метода GET /accounting
        """
        parser = ParserNalogJson()
        accounting = parser.parse_accounting(inn)
        return accounting
