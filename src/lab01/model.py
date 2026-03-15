class Book:
    # Атрибут класса
    MAX_PRICE = 10000  # максимальная стоимость книги
    MIN_YEAR = 1400    # примерное начало книгопечатания
    
    def __init__(self, title: str, author: str, year: int, pages: int, price: float):
        self._title = None
        self._author = None
        self._year = None
        self._pages = None
        self._price = None
        self.is_available = True  # состояние: доступна ли книга
        
        # устанавливаем через свойства
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.price = price
    
    # Методы валидации
    def _validate_title(self, value):
        if not isinstance(value, str):
            raise TypeError("Название должно быть строкой")
        if not value.strip():
            raise ValueError("Название не может быть пустым")
    
    def _validate_author(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя автора должно быть строкой")
        if not value.strip():
            raise ValueError("Имя автора не может быть пустым")
    
    def _validate_year(self, value):
        if not isinstance(value, int):
            raise TypeError("Год должен быть целым числом")
        if value < self.MIN_YEAR or value > 2026:  # текущий год
            raise ValueError(f"Год должен быть от {self.MIN_YEAR} до 2026")
    
    def _validate_pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        if value > 10000:  # разумный предел
            raise ValueError("Слишком много страниц")
    
    def _validate_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        if value > self.MAX_PRICE:
            raise ValueError(f"Цена не может превышать {self.MAX_PRICE}")
    
    # Свойства
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._validate_title(value)
        self._title = value.strip()
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._validate_author(value)
        self._author = value.strip()
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        self._validate_year(value)
        self._year = value
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, value):
        self._validate_pages(value)
        self._pages = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._validate_price(value)
        self._price = float(value)
    
    # Магические методы
    def __str__(self):
        status = "Доступна" if self.is_available else "Выдана"
        return f"📚 {self.title} - {self.author} ({self.year}) | {self.pages} стр. | {self.price:.2f} руб. | {status}"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        # Книги считаются одинаковыми, если совпадают название и автор
        return self.title == other.title and self.author == other.author
    
    # Бизнес-методы
    def get_age_category(self):
        """Определяет возрастную категорию книги"""
        current_year = 2026
        age = current_year - self.year
        if age < 5:
            return "Новинка"
        elif age < 20:
            return "Современная"
        elif age < 50:
            return "Классика"
        else:
            return "Антиквариат"
    
    def apply_discount(self, percent):
        """Применить скидку к книге"""
        if not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self.price = self.price * (1 - percent / 100)
        print(f"Цена снижена на {percent}%")
    
    def borrow(self):
        """Взять книгу (изменение состояния)"""
        if not self.is_available:
            raise Exception("Книга уже выдана")
        self.is_available = False
        print(f"Книга '{self.title}' выдана")
    
    def return_book(self):
        """Вернуть книгу"""
        if self.is_available:
            print("Книга и так в библиотеке")
            return
        self.is_available = True
        print(f"Книга '{self.title}' возвращена")
    
    def is_expensive(self):
        """Проверка, дорогая ли книга"""
        return self.price > 1000

# Пример demo.py
def demo():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА BOOK")
    print("=" * 60)
    
    # Создание объектов
    book1 = Book("Война и мир", "Лев Толстой", 1869, 1300, 1500.0)
    book2 = Book("Преступление и наказание", "Ф. Достоевский", 1866, 672, 800.0)
    
    print("\n--- Созданные книги ---")
    print(book1)
    print(book2)
    print(repr(book1))
    
    print("\n--- Сравнение книг ---")
    book3 = Book("Война и мир", "Лев Толстой", 2000, 500, 500.0)
    print(f"book1 == book2: {book1 == book2}")
    print(f"book1 == book3: {book1 == book3}")  # True, потому что название и автор совпадают
    
    print("\n--- Изменение свойств (setter) ---")
    print(f"Старая цена: {book1.price}")
    book1.price = 1800.0
    print(f"Новая цена: {book1.price}")
    
    # Проверка валидации
    try:
        book1.price = 20000  # слишком дорого
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    print("\n--- Атрибут класса ---")
    print(f"Максимальная цена (через класс): {Book.MAX_PRICE}")
    print(f"Максимальная цена (через экземпляр): {book1.MAX_PRICE}")
    
    print("\n--- Бизнес-логика ---")
    print(f"Категория '{book1.title}': {book1.get_age_category()}")
    
    # Изменение состояния
    print(f"\n--- Работа с состоянием ---")
    print(book1)
    book1.borrow()
    print(book1)
    
    try:
        book1.borrow()  # повторная выдача
    except Exception as e:
        print(f"Ошибка: {e}")
    
    book1.return_book()
    print(book1)
    
    print("\n--- Скидка ---")
    book1.apply_discount(10)
    print(book1)
    
    print("\n--- Проверка валидации при создании ---")
    test_cases = [
        ("Пустое название", {"title": "   ", "author": "Автор", "year": 2000, "pages": 100, "price": 500}),
        ("Отрицательные страницы", {"title": "Книга", "author": "Автор", "year": 2000, "pages": -10, "price": 500}),
        ("Год из будущего", {"title": "Книга", "author": "Автор", "year": 3000, "pages": 100, "price": 500}),
        ("Отрицательная цена", {"title": "Книга", "author": "Автор", "year": 2000, "pages": 100, "price": -100}),
    ]
    
    for desc, params in test_cases:
        try:
            Book(**params)
            print(f"[{desc}] НЕ ОЖИДАЛОСЬ - должно быть ошибкой")
        except (TypeError, ValueError) as e:
            print(f"[{desc}] УСПЕШНО: {e}")

if __name__ == "__main__":
    demo()