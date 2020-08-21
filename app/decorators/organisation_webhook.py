import requests
from configs.contacts import contacts
from app.exceptions.invalid_data import InvalidInn, InvalidAccId, InvalidOrgId


def organisation_webhook(func):
    """
    Декоратор для отправки webhook на OrganisationService.
    """
    def wrapper(*args, **kwargs):
        message = {'success': False}
        try:
            f = func(*args, **kwargs)
            send_message('organisation', message)
            message = {'success': True}
            return f

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
