import httpx

from temp.tools.fakers import get_random_email

user = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=user)
print(response.status_code)
print(response.json())