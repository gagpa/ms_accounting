from ..bussiness_objects import AccountingGetter, ResponseDealer


class AccountingLogic:
    """
    Логика получения БО.
    """

    def get_accounting(self, inn: str) -> dict:
        """
        Логика метода GET /accounting
        """
        ag = AccountingGetter(inn)
        accounting = ag.from_db()
        if accounting:
            response = ResponseDealer.accounting(data=accounting)
        else:
            ag.task_parse()
            response = ResponseDealer.in_queue()
        return response
