from ..bussiness_components import Accounting, NalogValidatorInfo, ResponseDealer
from ..exceptions.invalid_data import InvalidInn
from app.tasks.nalog_tasks import task_get_accounting
from app.schemas.response_accounting_schema import ResponseAccountingSchema


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
                accounting = Accounting.get_dict(inn)
                response = ResponseAccountingSchema().dumps()
            else:
                task_get_accounting.apply_async((inn,))
                response = ResponseDealer.in_queue()
            return response
        except InvalidInn:
            raise InvalidInn
