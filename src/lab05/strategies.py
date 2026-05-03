"""
Стратегии для сортировки, фильтрации и обработки книг.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import PrintedBook, Ebook, AudioBook


# ========== Стратегии сортировки ==========

def by_title(book):
    """Сортировка по названию."""
    return book.title


def by_author(book):
    """Сортировка по автору."""
    return book.author


def by_year(book):
    """Сортировка по году издания."""
    return book.year


def by_price(book):
    """Сортировка по цене."""
    return book.price


def by_price_then_title(book):
    """Сортировка сначала по цене, затем по названию."""
    return (book.price, book.title)


def by_year_then_title(book):
    """Сортировка сначала по году, затем по названию."""
    return (book.year, book.title)


# ========== Стратегии фильтрации ==========

def is_available(book):
    """Фильтр: только доступные книги."""
    return book.is_available


def is_borrowed(book):
    """Фильтр: только выданные книги."""
    return not book.is_available


def is_expensive(book, threshold=1000):
    """Фильтр: книги дороже порога (замыкание)."""
    return book.price > threshold


def is_cheap(book, threshold=500):
    """Фильтр: книги дешевле порога (замыкание)."""
    return book.price < threshold


def is_printed(book):
    """Фильтр: только печатные книги."""
    return isinstance(book, PrintedBook)


def is_ebook(book):
    """Фильтр: только электронные книги."""
    return isinstance(book, Ebook)


def is_audiobook(book):
    """Фильтр: только аудиокниги."""
    return isinstance(book, AudioBook)


# ========== Фабрики функций (задание на 4) ==========

def make_price_filter(max_price):
    """
    Фабрика функций: создаёт фильтр по максимальной цене.
    
    Args:
        max_price: максимальная цена
    
    Returns:
        функция-фильтр, принимающая книгу и возвращающая True, если цена <= max_price
    """
    def filter_fn(item):
        return item.price <= max_price
    return filter_fn


def make_year_filter(min_year, max_year):
    """
    Фабрика функций: создаёт фильтр по диапазону годов.
    
    Args:
        min_year: минимальный год
        max_year: максимальный год
    
    Returns:
        функция-фильтр, принимающая книгу и возвращающая True, если год в диапазоне
    """
    def filter_fn(item):
        return min_year <= item.year <= max_year
    return filter_fn


def make_discount_strategy(percent):
    """
    Фабрика функций: создаёт стратегию применения скидки.
    
    Args:
        percent: процент скидки
    
    Returns:
        функция, применяющая скидку к книге
    """
    def apply_discount(book):
        book.apply_discount(percent)
        return book
    return apply_discount


# ========== Callable-объекты-стратегии (задание на 5) ==========

class DiscountStrategy:
    """Стратегия применения скидки (callable-объект)."""
    
    def __init__(self, percent):
        """
        Args:
            percent: процент скидки
        """
        self.percent = percent
    
    def __call__(self, book):
        """Применяет скидку к книге."""
        book.apply_discount(self.percent)
        return book


class PriceExtractor:
    """Стратегия извлечения цены (callable-объект)."""
    
    def __call__(self, book):
        return book.price


class TitleExtractor:
    """Стратегия извлечения названия (callable-объект)."""
    
    def __call__(self, book):
        return book.title


# ========== Функции для map (преобразование) ==========

def to_string(book):
    """Преобразует книгу в строку через to_string()."""
    return book.to_string()


def to_tuple(book):
    """Преобразует книгу в кортеж (название, автор, цена)."""
    return (book.title, book.author, book.price)


def to_dict(book):
    """Преобразует книгу в словарь."""
    return {
        'title': book.title,
        'author': book.author,
        'year': book.year,
        'price': book.price
    }


def apply_10_percent_discount(book):
    """Применяет скидку 10% к книге."""
    book.apply_discount(10)
    return book