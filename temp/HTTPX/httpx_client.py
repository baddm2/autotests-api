import httpx

# 1 Проходим аутентификацию и получаем токен

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login response status code: {login_response.status_code}")
print(f"Login response: {login_response_data}")
access_token = login_response_data["token"]["accessToken"]

# создаем клиент

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=10,
    headers={"Authorization": f"Bearer {access_token}"}
)

# инициализируем клиент

get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()
print(get_user_me_response_data)
