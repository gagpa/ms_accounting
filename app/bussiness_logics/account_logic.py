from ..bussiness_components import Accounting, NalogValidatorInfo
from ..exceptions.invalid_app import InternalError
from ..exceptions.invalid_data import InvalidInn, InvalidOrgId, InvalidAccId
from app.tasks.nalog_parse_accounting import parse_accounting


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
                return accounting
            else:
                parse_accounting.apply_async((inn,))
                return {'data': 'Задачи в очереди.'}
        except InvalidInn:
            raise InvalidInn
