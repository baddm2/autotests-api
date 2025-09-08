import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "Новая задача1",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data) # передаем словарь  и указываем что это джейсон/ сам httpx уже переделывает словарь в джейсон для отправки запроса
# print(response.status_code)
# print(response.json())
#
# data1 = {"username": "test_user", "password": "12345"}
# response = httpx.post("https://httpbin.org/post", data=data1) # dla peredachi zaprosa v multiformdata
# print(response.status_code)
# print(response.request.headers)
# print(response.json())
#
#
# # для передачи заголовков
#
# headers = {"Authorization": "Bearer mytoken"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# print(response.request.headers)
# print(response.json())

#
# # для передачи запроса с параметрами / query
# params = {"userId": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.url)
# print(response.json())
#
# # отправка файлов
# file = {"file":("example.txt", open("example.txt", "rb"))}
# response = httpx.post("https://httpbin.org/post", files=file)
# print(response.json())

# работа с сессиями

# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())
# print(response2.json())
#
# # если нужно каждый раз передавать одни и теже параметры? например зоголовки
#
# client = httpx.Client(headers={"Content-Type": "application/json"})
# response = client.get("https://httpbin.org/get")
# print(response.json())
# client.close()

# работа с ошибками
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/ffdffgd")
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print("Ошибка запроса", e)

# работа с таймаутами
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout as e:
    print("Запрос превысил допустимое время", e)