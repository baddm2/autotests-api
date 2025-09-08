from typing import TypedDict

from httpx import Request, Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с открытыми методами в /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает пользователя в системе/

        :param request: Данные пользователя.
        :return: Ответ от сервера в виде объек httpx.Response.
        """
        return self.post("/api/v1/users", json = request)