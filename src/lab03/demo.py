import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import PrintedBook, Ebook, AudioBook
from lab02.collection import Library


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


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №3")
    print("Наследование и иерархия классов (Книги)")
    print("=" * 60)

    print_separator("СЦЕНАРИЙ 1: Создание объектов разных типов")

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

    print_separator("СЦЕНАРИЙ 2: Коллекция + полиморфизм")

    library = Library("Медиатека")

    library.add(printed)
    library.add(ebook)
    library.add(audiobook)

    print_collection(library, "Все объекты в коллекции")

    print("\nПроверка типов (isinstance):")
    for book in library:
        if isinstance(book, PrintedBook):
            print(f"  Печатная книга: {book.title}")
        elif isinstance(book, Ebook):
            print(f"  Электронная книга: {book.title}")
        elif isinstance(book, AudioBook):
            print(f"  Аудиокнига: {book.title}")

    print_separator("СЦЕНАРИЙ 3: Уникальные методы")

    print(f"  Вес для доставки '{printed.title}': {printed.get_shipping_weight():.2f} кг")
    print(f"  Время скачивания '{ebook.title}': {ebook.get_download_time():.2f} сек")
    print(f"  Оставшееся время '{audiobook.title}': {audiobook.get_remaining_time(3.5):.1f} ч")

    print_separator("ИТОГ")
    print("Все требования выполнены:")
    print("  - Оценка 3: базовый класс + 2 дочерних, super(), новые атрибуты и методы")
    print("  - Оценка 4: переопределение __str__, isinstance(), коллекция из ЛР-2")
    print("  - Оценка 5: единый интерфейс, фильтрация по типу")
    print(f"\nФинальное состояние: {library}")
    print_collection(library, "Текущий каталог")


if __name__ == "__main__":
    main()