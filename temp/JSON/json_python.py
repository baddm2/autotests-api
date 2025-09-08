import json

# Десериализация / парсинг JSON-строки в Python-объект (dict)
json_data = '{"name": "Иван", "age":30, "is_student":false}'  # это строка
parsed_data = json.loads(json_data)
# {'name': 'Иван', 'age': 30, 'is_student': False}

# Чтнение JSON из файла
with open("data.json", "r", encoding="utf-8") as file:  # открываем файл на чтение
    data = json.load(file)  # вызываем метод лоадб который поможет из байтов файла получить словарь
    print(data, type(data))
    # {'name': 'Peter', 'city': 'Spb', 'zip': 123123} <class 'dict'>

# Сериализация /  сохранение JSON из Python-объект (dict)
dict_data = {
    'name': 'Мария',
    'age': 35,
    'is_student': None
}
json_string = json.dumps(dict_data, indent=4)  # добавляем отсутпы с помощью indent
print(json_string)
# {"name": "Maria", "age": 35, "is_student": true}

# Запись JSON в файл
with open("create_json.json", "w", encoding="utf-8") as file: # открываем файл на запись
    json.dump(dict_data, file, indent=4, ensure_ascii=False)



























