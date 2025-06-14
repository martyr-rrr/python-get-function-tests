from src.functions import get_function

get = get_function()

assert get({"hello": "world"}, "hello") == "world", "Должен возвращать значение по существующему ключу"

assert get({}, "hello", "kitty") == "kitty", "Должен возвращать значение по умолчанию"

assert get({"hello": "world"}, "hello", "kitty") == "world", "Должен игнорировать default_value если ключ существует"

print("✅ Все тесты прошли успешно!")
