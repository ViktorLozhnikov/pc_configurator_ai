import json

def load_components():
    try:
        with open('backend/components.json', 'r', encoding='utf-8') as file:
            return json.load(file)["components"]
    except FileNotFoundError:
        return {"error": "Файл components.json не знайдено."}
    except json.JSONDecodeError:
        return {"error": "Помилка у форматі JSON."}
