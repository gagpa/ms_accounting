import requests

from app.exceptions import InvalidInn, InvalidAccId, InvalidOrgId
from app.schemas.accounting_schema import AccountingSchema
from configs.contacts import contacts


def organisation_webhook(func):
    """
    Декоратор для отправки webhook на OrganisationService.
    """

    def wrapper(*args, **kwargs):
        message = {
            'success': False,
            'data': {'inn': args[0]}
        }
        try:
            accounting = func(*args, **kwargs)
            message = AccountingSchema().dump({'inn': accounting['inn'],
                                               'period': accounting['period'],
                                               'accounting': accounting['accounting']
                                               })
            send_message('organisation', message)
            return accounting

        except ConnectionError:
            pass
        except InvalidInn:
            pass
        except (InvalidAccId, InvalidOrgId):
            pass

        send_message('organisation', message)

    return wrapper


def send_message(contact_name, message):
    """
    Отправить сообщение.
    """
    contact_link = contacts[contact_name]
    response = requests.get(contact_link, json=message)
    return is_success(response)


def is_success(response):
    """
    Проверить ответ.
    """
    return response.status_code == 200
