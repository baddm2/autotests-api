import httpx


# Получение токенов
login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login response status code: {login_response.status_code}")
print(f"Login response: {login_response_data}")

# # обновление токена
# refresh_payload ={
#     "refreshToken": login_response_data["token"]["refreshToken"]
# }
#
# refresh_token_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
# refresh_token_response_data = refresh_token_response.json()
# print(f"Refresh token response status code: {refresh_token_response.status_code}")
# print(f"Refresh token response: {refresh_token_response_data}")

# запрос на получение информации о текущем пользователе

response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"})
print(response.status_code)
print(response.json())