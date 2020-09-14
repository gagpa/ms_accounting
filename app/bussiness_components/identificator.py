from configs.contacts import contacts
from app.exceptions import InvalidToken


class Identificator:
    """
    Идентифицирует пользователей.
    """

    __contacts = contacts

    def __init__(self, token: str):
        """
        Проверяет токен. Существует такой или нет.
        """
        token = token or ''
        contact = self.__contacts.get(token, False)
        if contact is False:
            raise InvalidToken
        self.contact = self.__contacts.get(token)

    def get_contact(self) -> str:
        """
        Вернуть URL контакта.
        """
        return self.contact
