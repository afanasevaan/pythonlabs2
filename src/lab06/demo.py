"""
Лабораторная работа №6
Generics и typing

Демонстрация работы TypedCollection.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab03.models import PrintedBook, Ebook, AudioBook
from container import TypedCollection, DisplayableCollection, ScorableCollection, Displayable, Scorable


def print_separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def print_collection(collection: TypedCollection, label: str = "Элементы"):
    print(f"\n{label} ({len(collection)} шт.):")
    if len(collection) == 0:
        print("  (пусто)")
    for item in collection:
        print(f"  - {item}")


def create_sample_books():
    """Создаёт список тестовых книг."""
    return [
        PrintedBook("Война и мир", "Лев Толстой", 1869, 1300, 1500.0, "твердый", 5000),
        PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 672, 800.0, "мягкий", 10000),
        Ebook("1984", "Джордж Оруэлл", 1949, 328, 450.0, "EPUB", 2.5),
        Ebook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 300.0, "PDF", 1.2),
        AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 1200.0, 12.5, "Константин Хабенский"),
    ]


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №6")
    print("Generics и typing")
    print("=" * 60)

    # ========== СЦЕНАРИЙ 1: Базовые операции (оценка 3) ==========
    print_separator("СЦЕНАРИЙ 1: Базовые операции TypedCollection")

    books = create_sample_books()
    
    # Создаём типизированную коллекцию для книг
    collection: TypedCollection[PrintedBook] = TypedCollection("Мои книги")
    
    # Добавляем книги
    for book in books[:3]:  # добавляем только первые 3 книги
        collection.add(book)
        print(f"Добавлено: {book.display() if hasattr(book, 'display') else book}")
    
    print(f"\nВсего элементов: {len(collection)}")
    print_collection(collection, "Содержимое коллекции")
    
    # Проверка валидации типов (при попытке добавить объект другого типа)
    print("\nПроверка типов (добавление объекта неправильного типа):")
    try:
        collection.add("это не книга")  # type: ignore
    except Exception as e:
        print(f"  Ошибка (ожидаемо): {e}")

    # ========== СЦЕНАРИЙ 2: find, filter, map (оценка 4) ==========
    print_separator("СЦЕНАРИЙ 2: find, filter, map")

    # Создаём коллекцию со всеми книгами
    all_books: TypedCollection = TypedCollection("Все книги")
    for book in books:
        all_books.add(book)
    
    # find() — поиск первого подходящего
    print("\n1. find() — поиск по условию:")
    found = all_books.find(lambda b: b.year > 1900)
    print(f"  Первая книга после 1900 года: {found.display() if hasattr(found, 'display') else found}")
    
    not_found = all_books.find(lambda b: b.year > 2100)
    print(f"  Книга после 2100 года (не найдена): {not_found}")
    
    # filter() — фильтрация
    print("\n2. filter() — фильтрация по условию:")
    expensive_books = all_books.filter(lambda b: b.price > 1000)
    print(f"  Книги дороже 1000 руб. ({len(expensive_books)} шт.):")
    for book in expensive_books:
        print(f"    - {book.display() if hasattr(book, 'display') else book}")
    
    # map() — преобразование (демонстрация смены типа)
    print("\n3. map() — преобразование (демонстрация смены типа):")
    
    # map: TypedCollection[Book] -> list[str] (названия)
    titles = all_books.map(lambda b: b.title)
    print(f"  Названия книг (list[str]): {titles}")
    
    # map: TypedCollection[Book] -> list[float] (цены со скидкой 10%)
    discounted_prices = all_books.map(lambda b: b.price * 0.9)
    print(f"  Цены со скидкой 10% (list[float]): {[f'{p:.2f}' for p in discounted_prices]}")
    
    # map: TypedCollection[Book] -> list[int] (годы)
    years = all_books.map(lambda b: b.year)
    print(f"  Годы издания (list[int]): {years}")
    
    # ========== СЦЕНАРИЙ 3: Protocols (оценка 5) ==========
    print_separator("СЦЕНАРИЙ 3: Protocols (структурная типизация)")
    
    print("\n1. DisplayableCollection — коллекция объектов с методом display():")
    displayable_collection = DisplayableCollection("Отображаемые объекты")
    
    # Добавляем объекты разных типов (у всех есть метод display())
    for book in books:
        displayable_collection.add(book)
        print(f"  Добавлен: {book.display()}")
    
    print(f"\n  Всего объектов в коллекции: {len(displayable_collection)}")
    
    # Вызов метода display() для каждого объекта
    print("\n  Вызов display() для всех объектов:")
    for item in displayable_collection:
        print(f"    {item.display()}")
    
    print("\n2. ScorableCollection — коллекция объектов с методом score():")
    scorable_collection = ScorableCollection("Оцениваемые объекты")
    
    for book in books:
        scorable_collection.add(book)
        print(f"  Добавлен: {book.display()} | score = {book.score()}")
    
    print("\n  Сортировка по score() (по убыванию):")
    scorable_collection.sort_by(lambda b: b.score(), reverse=True)
    for item in scorable_collection:
        print(f"    {item.display()} -> {item.score()}")
    
    # ========== ИТОГ ==========
    print_separator("ИТОГ")
    print("Все требования выполнены:")
    print("  - Оценка 3: аннотации типов, TypedCollection, базовые методы")
    print("  - Оценка 4: find, filter, map (с демонстрацией смены типа R)")
    print("  - Оценка 5: Protocols (Displayable, Scorable), TypeVar с bound")
    print(f"\nФинальное состояние: {all_books}")
    print_collection(all_books, "Текущий каталог")


if __name__ == "__main__":
    main()