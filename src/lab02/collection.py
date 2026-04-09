from typing import List, Optional, Callable
from model import Book


class Library:
    def __init__(self, name: str = "Библиотека"):
        self.name = name
        self._items: List[Book] = []

    def add(self, item: Book) -> None:
        if not isinstance(item, Book):
            raise TypeError(f"Можно добавлять только Book, получен {type(item).__name__}")

        for existing in self._items:
            if existing == item:
                raise ValueError(f"Книга уже существует: '{item.title}' - {item.author}")

        self._items.append(item)

    def remove(self, item: Book) -> None:
        if item not in self._items:
            raise ValueError("Такой книги нет в коллекции")
        self._items.remove(item)

    def remove_at(self, index: int) -> None:
        if not (0 <= index < len(self._items)):
            raise IndexError(f"Индекс {index} вне диапазона")
        del self._items[index]

    def get_all(self) -> List[Book]:
        return self._items.copy()

    def find_by_title(self, title: str) -> Optional[Book]:
        for book in self._items:
            if book.title == title:
                return book
        return None

    def find_by_author(self, author: str) -> List[Book]:
        return [book for book in self._items if book.author == author]

    def find_by_year(self, year: int) -> List[Book]:
        return [book for book in self._items if book.year == year]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> Book:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if not (0 <= index < len(self._items)):
            raise IndexError(f"Индекс {index} вне диапазона")
        return self._items[index]

    def sort(self, key: Optional[Callable[[Book], any]] = None, reverse: bool = False) -> None:
        if key is None:
            self._items.sort(reverse=reverse)
        else:
            self._items.sort(key=key, reverse=reverse)

    def filter(self, predicate: Callable[[Book], bool]) -> 'Library':
        new_library = Library(f"{self.name} (фильтр)")
        for book in self._items:
            if predicate(book):
                new_library.add(book)
        return new_library

    def get_available(self) -> 'Library':
        return self.filter(lambda b: b.is_available)

    def get_borrowed(self) -> 'Library':
        return self.filter(lambda b: not b.is_available)

    def get_expensive(self, threshold: float = 1000) -> 'Library':
        return self.filter(lambda b: b.price > threshold)

    def get_by_age_category(self, category: str) -> 'Library':
        return self.filter(lambda b: b.get_age_category() == category)

    def __str__(self) -> str:
        return f"{self.name}: {len(self._items)} книг"

    def __repr__(self) -> str:
        return f"Library(name='{self.name}', books={len(self._items)})"