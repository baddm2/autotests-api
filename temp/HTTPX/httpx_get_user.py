import httpx

from temp.tools.fakers import get_random_email


# 1. Создаем юзера
user = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=user)
create_user_response_data = create_user_response.json()
print(create_user_response.status_code)
print(f"Создан пользователь: {create_user_response_data}")

# 2. Проходим аутентификацию и получаем токен

login_payload = {
    "email": user["email"],
    "password": user["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login response status code: {login_response.status_code}")
print(f"Login response: {login_response_data}")



# 3. Получаем инфу о юзере по его идентификатору

userId = create_user_response_data["user"]["id"]
token = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}

get_user_response = httpx.get(f"http://localhost:8000/api/v1/users/{userId}", headers=token)
get_user_response_data = get_user_response.json()

print(f"Информация о пользователе: {get_user_response_data}")