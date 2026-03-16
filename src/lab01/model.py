from validate import (
    validate_title,
    validate_author,
    validate_year,
    validate_pages,
    validate_price
)

class Book:
    MAX_PRICE = 10000
    MIN_YEAR = 1400

    def __init__(self, title: str, author: str, year: int, pages: int, price: float):
        self._title = None
        self._author = None
        self._year = None
        self._pages = None
        self._price = None
        self.is_available = True

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        validate_title(value)
        self._title = value.strip()

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        validate_author(value)
        self._author = value.strip()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        validate_year(value)
        self._year = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        validate_pages(value)
        self._pages = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        validate_price(value)
        self._price = float(value)

    def str(self):
        status = "Доступна" if self.is_available else "Выдана"
        return f"📚 {self.title} - {self.author} ({self.year}) | {self.pages} стр. | {self.price:.2f} руб. | {status}"

    def repr(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

    def eq(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def get_age_category(self):
        age = 2026 - self.year
        if age < 5:
            return "Новинка"
        elif age < 20:
            return "Современная"
        elif age < 50:
            return "Классика"
        else:
            return "Антиквариат"

    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self.price = self.price * (1 - percent / 100)
        print(f"Цена снижена на {percent}%")

    def borrow(self):
        if not self.is_available:
            raise Exception("Книга уже выдана")
        self.is_available = False
        print(f"Книга '{self.title}' выдана")

    def return_book(self):
        if self.is_available:
            print("Книга и так в библиотеке")
            return
        self.is_available = True
        print(f"Книга '{self.title}' возвращена")

    def is_expensive(self):
        return self.price > 1000