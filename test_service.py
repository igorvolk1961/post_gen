import requests

topic = "Чипы для ИИ"

#url = "http://localhost:8000/generate-post"
url = "https://dreadful-anestassia-igorvolk-9eb2dc2a.koyeb.app//generate-post"
response = requests.post(url, json={'topic': topic})  # Выполняем POST-запрос к API
if response.status_code != 200:
    # Если статус код не 200, выводим ошибку
    print(f"Ошибка при получении данных: {response.text}")
else:
    # Извлекаем сгенерированный контент из ответа
    data = response.json()
    print("Заголовок:", data.get("title"))
    print("\nМета-описание:", data.get("meta_description"))
    print("\nСодержание статьи:")
    print(data.get("post_content"))
