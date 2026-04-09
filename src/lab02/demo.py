from model import Book
from collection import Library


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
    print("ЛАБОРАТОРНАЯ РАБОТА №2")
    print("Коллекция объектов (Книги -> Библиотека)")
    print("=" * 60)

    books = [
        Book("Война и мир", "Лев Толстой", 1869, 1300, 1500.0),
        Book("Преступление и наказание", "Фёдор Достоевский", 1866, 672, 800.0),
        Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 480, 1200.0),
        Book("1984", "Джордж Оруэлл", 1949, 328, 950.0),
        Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, 450.0),
        Book("Три товарища", "Эрих Мария Ремарк", 1936, 480, 1100.0),
    ]

    print("\nСОЗДАНИЕ КНИГ")
    print("-" * 40)
    for book in books:
        print(f"  OK: {book}")

    # Сценарий 1
    print_separator("СЦЕНАРИЙ 1: Базовые операции")

    library = Library("Моя библиотека")

    for book in books:
        library.add(book)
    print(f"Добавлено {len(library)} книг")

    print_collection(library, "Все книги")

    book_to_remove = books[2]
    print(f"\nУдаляем: {book_to_remove.title}")
    library.remove(book_to_remove)
    print_collection(library, "После удаления")

    print("\nПроверка защиты от дубликатов:")
    try:
        duplicate = Book("Война и мир", "Лев Толстой", 2000, 500, 100.0)
        library.add(duplicate)
    except ValueError as e:
        print(f"  Ошибка (ожидаемо): {e}")

    print("\nПроверка типа добавляемого объекта:")
    try:
        library.add("это не книга")
    except TypeError as e:
        print(f"  Ошибка (ожидаемо): {e}")

    # Сценарий 2
    print_separator("СЦЕНАРИЙ 2: Поиск, итерация, len()")

    library.add(books[2])

    print(f"Количество книг: {len(library)}")

    print("\nПОИСК:")
    found = library.find_by_title("1984")
    print(f"  По названию '1984': {found}")

    author_books = library.find_by_author("Лев Толстой")
    print(f"  По автору 'Лев Толстой': {len(author_books)} книг")
    for b in author_books:
        print(f"    - {b.title}")

    print("\nИтерация через for:")
    for idx, book in enumerate(library):
        print(f"  {idx+1}. {book.title} - {book.author} ({book.year})")

    # Сценарий 3
    print_separator("СЦЕНАРИЙ 3: Индексация, сортировка, фильтрация")

    print("ИНДЕКСАЦИЯ:")
    print(f"  Первая книга: {library[0].title}")
    print(f"  Третья книга: {library[2].title}")

    print("\nСОРТИРОВКА:")
    library.sort(key=lambda b: b.year)
    print("  По году (возрастание):")
    for book in library:
        print(f"    {book.year} - {book.title}")

    library.sort(key=lambda b: b.price)
    print("\n  По цене (возрастание):")
    for book in library:
        print(f"    {book.price:.0f} руб. - {book.title}")

    library.sort(key=lambda b: b.title, reverse=True)
    print("\n  По названию (убывание):")
    for book in library:
        print(f"    {book.title}")

    books[0].borrow()
    books[4].borrow()

    available = library.get_available()
    print_collection(available, "Доступные книги")

    borrowed = library.get_borrowed()
    print_collection(borrowed, "Выданные книги")

    expensive = library.get_expensive(1000)
    print_collection(expensive, "Дорогие книги (>1000 руб.)")

    print("\nФильтр по категориям:")
    for category in ['Новинка', 'Современная', 'Классика', 'Антиквариат']:
        cat_books = library.get_by_age_category(category)
        if len(cat_books) > 0:
            print(f"  {category}: {[b.title for b in cat_books]}")

    print("\nПроизвольная фильтрация:")
    modern_classics = library.filter(lambda b: 1900 <= b.year <= 1950)
    print_collection(modern_classics, "Классика XX века (1900-1950)")

    print_separator("ИТОГ")
    print("Все требования выполнены:")
    print("  - Оценка 3: add, remove, get_all, проверка типа")
    print("  - Оценка 4: find_by_*, __len__, __iter__, защита от дубликатов")
    print("  - Оценка 5: __getitem__, remove_at, sort, filter")
    print(f"\nФинальное состояние: {library}")
    print_collection(library, "Текущий каталог")


if __name__ == "__main__":
    main()