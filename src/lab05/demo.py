import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import PrintedBook, Ebook, AudioBook
from collection import Library  # ← исправлено: своя коллекция из lab05
from strategies import (
    by_title, by_author, by_year, by_price,
    is_available, is_printed, make_price_filter,
    DiscountStrategy, to_string, to_tuple, apply_10_percent_discount
)


def print_separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def print_collection(library: Library, label: str = "Книги"):
    print(f"\n{label} ({len(library)} шт.):")
    if len(library) == 0:
        print("  (пусто)")
    for book in library:
        print(f"  - {book}")


def create_sample_library() -> Library:
    """Создаёт библиотеку с тестовыми книгами."""
    library = Library("Моя библиотека")
    
    books = [
        PrintedBook("Война и мир", "Лев Толстой", 1869, 1300, 1500.0, "твердый", 5000),
        PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 672, 800.0, "мягкий", 10000),
        Ebook("1984", "Джордж Оруэлл", 1949, 328, 450.0, "EPUB", 2.5),
        Ebook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 300.0, "PDF", 1.2),
        AudioBook("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 1200.0, 12.5, "Константин Хабенский"),
        AudioBook("Три товарища", "Эрих Мария Ремарк", 1936, 480, 1100.0, 10.0, "Алексей Багдасаров"),
        PrintedBook("Анна Каренина", "Лев Толстой", 1877, 864, 900.0, "твердый", 8000),
        Ebook("Собачье сердце", "Михаил Булгаков", 1925, 150, 250.0, "FB2", 0.8),
    ]
    
    for book in books:
        library.add(book)
    
    return library


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5")
    print("Функции как аргументы. Стратегии и делегаты.")
    print("=" * 60)
    
    # Сценарий 1: Сортировка
    print_separator("СЦЕНАРИЙ 1: Сортировка тремя разными стратегиями")
    
    lib2 = create_sample_library()
    lib2.sort_by(by_title)
    print_collection(lib2, "Сортировка по названию")
    
    lib3 = create_sample_library()
    lib3.sort_by(by_author)
    print_collection(lib3, "Сортировка по автору")
    
    lib4 = create_sample_library()
    lib4.sort_by(by_price)
    print_collection(lib4, "Сортировка по цене")
    
    # Сценарий 2: Фильтрация
    print_separator("СЦЕНАРИЙ 2: Фильтрация двумя разными стратегиями")
    
    lib6 = create_sample_library()
    lib6.filter_by(is_available)
    print_collection(lib6, "Только доступные книги")
    
    lib7 = create_sample_library()
    lib7.filter_by(is_printed)
    print_collection(lib7, "Только печатные книги")
    
    # Сценарий 3: Фабрика функций
    print_separator("СЦЕНАРИЙ 3: Фабрика функций")
    
    price_filter = make_price_filter(500)
    lib9 = create_sample_library()
    lib9.filter_by(price_filter)
    print_collection(lib9, "Книги дешевле 500 руб.")
    
    # Сценарий 4: Цепочка операций
    print_separator("СЦЕНАРИЙ 4: Цепочка filter -> sort -> apply")
    
    lib11 = create_sample_library()
    lib11.filter_by(is_available).sort_by(by_price).apply(apply_10_percent_discount)
    print_collection(lib11, "После цепочки операций")
    
    # Сценарий 5: Callable-объект
    print_separator("СЦЕНАРИЙ 5: Callable-объект как стратегия")
    
    lib12 = create_sample_library()
    lib12.filter_by(is_available).sort_by(by_price)
    discount_strategy = DiscountStrategy(15)
    lib12.apply(discount_strategy)
    print_collection(lib12, "После применения скидки 15%")
    
    # Итог
    print_separator("ИТОГ")
    print("Все требования выполнены:")
    print("  - Оценка 3: сортировка (3+ стратегии), фильтрация (2+ стратегии)")
    print("  - Оценка 4: map(), фабрика функций, sort_by/filter_by, lambda")
    print("  - Оценка 5: callable-стратегия, apply(), цепочка операций")


if __name__ == "__main__":
    main()