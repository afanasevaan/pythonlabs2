import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import PrintedBook, Ebook, AudioBook
from lab02.collection import Library
from interfaces import Printable, Comparable, Discountable


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


def print_all(items: list):
    """Универсальная функция, работающая через интерфейс Printable."""
    print("\nВывод через интерфейс Printable:")
    for item in items:
        if hasattr(item, 'to_string'):
            print(f"  {item.to_string()}")


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №4")
    print("Интерфейсы и абстрактные классы (ABC)")
    print("=" * 60)

    # Сценарий 1
    print_separator("СЦЕНАРИЙ 1: Создание объектов и вызов интерфейсных методов")

    printed = PrintedBook(
        "Война и мир", "Лев Толстой", 1869, 1300, 1500.0,
        binding="твердый", circulation=5000
    )

    ebook = Ebook(
        "1984", "Джордж Оруэлл", 1949, 328, 450.0,
        file_format="EPUB", file_size_mb=2.5
    )

    audiobook = AudioBook(
        "Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 1200.0,
        duration_hours=12.5, narrator="Константин Хабенский"
    )

    print("\nСозданные объекты:")
    print(f"  {printed}")
    print(f"  {ebook}")
    print(f"  {audiobook}")

    print("\nИнтерфейс Printable (to_string):")
    print(f"  {printed.to_string()}")
    print(f"  {ebook.to_string()}")
    print(f"  {audiobook.to_string()}")

    print("\nИнтерфейс Comparable (compare_to):")
    print(f"  Сравнение цен (1984 vs Война и мир): {ebook.compare_to(printed)}")

    print("\nИнтерфейс Discountable (apply_discount):")
    print(f"  Цена 1984 до скидки: {ebook.price:.2f} руб.")
    ebook.apply_discount(10)
    print(f"  Цена 1984 после скидки 10%: {ebook.price:.2f} руб.")

    # Сценарий 2
    print_separator("СЦЕНАРИЙ 2: Универсальная функция через интерфейс")

    printable_objects = [printed, ebook, audiobook]
    print_all(printable_objects)

    print("\nПроверка isinstance:")
    print(f"  printed реализует Printable? {isinstance(printed, Printable)}")
    print(f"  printed реализует Comparable? {isinstance(printed, Comparable)}")
    print(f"  printed реализует Discountable? {isinstance(printed, Discountable)}")

    # Сценарий 3
    print_separator("СЦЕНАРИЙ 3: Интеграция с коллекцией")

    library = Library("Медиатека")
    library.add(printed)
    library.add(ebook)
    library.add(audiobook)
    library.add(PrintedBook("Преступление и наказание", "Фёдор Достоевский", 1866, 672, 800.0, "мягкий", 10000))
    library.add(Ebook("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 300.0, "PDF", 1.2))

    print_collection(library, "Все книги в коллекции")

    # Фильтрация через list comprehension (без изменения коллекции)
    printable_in_library = [book for book in library if isinstance(book, Printable)]
    print(f"\nОбъекты, реализующие Printable ({len(printable_in_library)} шт.):")
    for item in printable_in_library:
        print(f"  - {item.to_string()}")

    print("\nПолиморфизм через интерфейс (вызов to_string для всех):")
    for book in library:
        print(f"  {book.to_string()}")

    print("\nСортировка по цене:")
    books_list = list(library)
    books_list.sort(key=lambda b: b.price)
    for book in books_list:
        print(f"  {book.price:.2f} руб. - {book.title}")

    # Итог
    print_separator("ИТОГ")
    print("Все требования выполнены:")
    print("  - Оценка 3: 2 интерфейса, абстрактные методы, реализация в классах")
    print("  - Оценка 4: интерфейс как тип, множественная реализация, isinstance()")
    print("  - Оценка 5: интеграция с коллекцией, полиморфизм через интерфейс")
    print(f"\nФинальное состояние: {library}")
    print_collection(library, "Текущий каталог")


if __name__ == "__main__":
    main()