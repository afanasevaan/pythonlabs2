MIN_YEAR = 1400
MAX_PRICE = 10000

def validate_title(value):
    if not isinstance(value, str):
        raise TypeError("Название должно быть строкой")
    if not value.strip():
        raise ValueError("Название не может быть пустым")

def validate_author(value):
    if not isinstance(value, str):
        raise TypeError("Имя автора должно быть строкой")
    if not value.strip():
        raise ValueError("Имя автора не может быть пустым")

def validate_year(value):
    if not isinstance(value, int):
        raise TypeError("Год должен быть целым числом")
    if value < MIN_YEAR or value > 2026:
        raise ValueError(f"Год должен быть от {MIN_YEAR} до 2026")

def validate_pages(value):
    if not isinstance(value, int):
        raise TypeError("Количество страниц должно быть целым числом")
    if value <= 0:
        raise ValueError("Количество страниц должно быть положительным")
    if value > 10000:
        raise ValueError("Слишком много страниц")

def validate_price(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")
    if value < 0:
        raise ValueError("Цена не может быть отрицательной")
    if value > MAX_PRICE:
        raise ValueError(f"Цена не может превышать {MAX_PRICE}")