from typing import List, Optional, Callable, Any
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import Book


class Library:
    """Коллекция книг с поддержкой функций-стратегий."""
    
    def __init__(self, name: str = "Библиотека"):
        self.name = name
        self._items: List[Book] = []

    # ========== Базовые операции ==========
    
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

    def get_all(self) -> List[Book]:
        return self._items.copy()

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

    # ========== Методы для ЛР-5 ==========
    
    def sort_by(self, key_func: Callable[[Book], Any], reverse: bool = False) -> 'Library':
        """Сортировка с использованием функции-ключа."""
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate: Callable[[Book], bool]) -> 'Library':
        """Фильтрация с использованием функции-предиката."""
        self._items = [book for book in self._items if predicate(book)]
        return self
    
    def apply(self, func: Callable[[Book], Any]) -> 'Library':
        """Применяет функцию ко всем элементам коллекции."""
        for book in self._items:
            func(book)
        return self
    
    def map_to(self, transform_func: Callable[[Book], Any]) -> List[Any]:
        """Преобразует коллекцию в список через map()."""
        return list(map(transform_func, self._items))
    
    def __str__(self) -> str:
        return f"{self.name}: {len(self._items)} книг"