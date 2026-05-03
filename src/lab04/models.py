import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Book as BaseBook
from lab04.interfaces import Printable, Comparable, Discountable


class Book(BaseBook, Printable, Comparable, Discountable):
    """Базовый класс Book с реализацией интерфейсов."""
    
    def to_string(self) -> str:
        return f"Книга: {self.title} - {self.author} ({self.year}) | {self.price:.2f} руб."
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Book):
            return 1
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0
    
    def apply_discount(self, percent: float) -> None:
        if not 0 <= percent <= 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self.price = self.price * (1 - percent / 100)


class PrintedBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, price: float,
                 binding: str, circulation: int):
        super().__init__(title, author, year, pages, price)
        self.binding = binding
        self.circulation = circulation
    
    def get_shipping_weight(self) -> float:
        return self.pages * 0.01
    
    def to_string(self) -> str:
        return f"[Печатная] {self.title} - {self.author} ({self.year}) | {self.pages} стр. | {self.price:.2f} руб. | Переплёт: {self.binding}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Book):
            return 1
        if self.year < other.year:
            return -1
        elif self.year > other.year:
            return 1
        return 0
    
    def __str__(self):
        return self.to_string()


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, price: float,
                 file_format: str, file_size_mb: float):
        super().__init__(title, author, year, pages, price)
        self.file_format = file_format
        self.file_size_mb = file_size_mb
    
    def get_download_time(self, speed_mbps: float = 10) -> float:
        return (self.file_size_mb * 8) / speed_mbps
    
    def to_string(self) -> str:
        return f"[Электронная] {self.title} - {self.author} ({self.year}) | {self.price:.2f} руб. | Формат: {self.file_format}"
    
    def apply_discount(self, percent: float) -> None:
        if not 0 <= percent <= 50:
            raise ValueError("Скидка на электронные книги не может превышать 50%")
        super().apply_discount(percent)
    
    def __str__(self):
        return self.to_string()


class AudioBook(Book):
    def __init__(self, title: str, author: str, year: int, pages: int, price: float,
                 duration_hours: float, narrator: str):
        super().__init__(title, author, year, pages, price)
        self.duration_hours = duration_hours
        self.narrator = narrator
    
    def get_remaining_time(self, listened_hours: float = 0) -> float:
        return max(0, self.duration_hours - listened_hours)
    
    def to_string(self) -> str:
        return f"[Аудио] {self.title} - {self.author} ({self.year}) | {self.price:.2f} руб. | Читает: {self.narrator}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, AudioBook):
            return 1
        if self.duration_hours < other.duration_hours:
            return -1
        elif self.duration_hours > other.duration_hours:
            return 1
        return 0
    
    def __str__(self):
        return self.to_string()