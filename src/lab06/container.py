from typing import TypeVar, Generic, Callable, Optional, List, Protocol
from lab03.models import Book, PrintedBook, Ebook, AudioBook
from lab04.models import Book as BookWithInterfaces




T = TypeVar('T')           # Тип элементов коллекции
R = TypeVar('R')           # Тип результата преобразования (для map)




class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить."""
    def display(self) -> str:
        """Возвращает строковое представление объекта."""
        ...


class Scorable(Protocol):
    """Протокол для объектов, которые можно оценить."""
    def score(self) -> float:
        """Возвращает числовую оценку объекта."""
        ...




D = TypeVar('D', bound=Displayable)   # Только объекты с методом display()
S = TypeVar('S', bound=Scorable)      # Только объекты с методом score()




class TypedCollection(Generic[T]):
    """
    Обобщённая коллекция, которая хранит элементы определённого типа T.
    
    Повторяет интерфейс коллекции из ЛР-2, но с аннотациями типов.
    """
    
    def __init__(self, name: str = "TypedCollection") -> None:
        """
        Конструктор коллекции.
        
        Args:
            name: название коллекции
        """
        self.name: str = name
        self._items: List[T] = []
    
    
    
    def add(self, item: T) -> None:
        """
        Добавить элемент в коллекцию.
        
        Args:
            item: элемент типа T
        
        Raises:
            ValueError: если элемент уже существует
        """
        if item in self._items:
            raise ValueError(f"Элемент уже существует в коллекции: {item}")
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        """
        Удалить элемент из коллекции.
        
        Args:
            item: элемент типа T
        
        Raises:
            ValueError: если элемент не найден
        """
        if item not in self._items:
            raise ValueError(f"Элемент не найден в коллекции: {item}")
        self._items.remove(item)
    
    def remove_at(self, index: int) -> None:
        """
        Удалить элемент по индексу.
        
        Args:
            index: индекс элемента
        
        Raises:
            IndexError: если индекс вне диапазона
        """
        if not (0 <= index < len(self._items)):
            raise IndexError(f"Индекс {index} вне диапазона")
        del self._items[index]
    
    def get_all(self) -> List[T]:
        """
        Вернуть копию списка всех элементов.
        
        Returns:
            список элементов типа T
        """
        return self._items.copy()
    
    
    
    def find_by_title(self, title: str) -> Optional[T]:
        """
        Поиск элемента по названию (для книг).
        
        Args:
            title: название книги
        
        Returns:
            элемент или None
        """
        for item in self._items:
            if hasattr(item, 'title') and item.title == title:
                return item
        return None
    
    def find_by_author(self, author: str) -> List[T]:
        """
        Поиск элементов по автору (для книг).
        
        Args:
            author: автор книги
        
        Returns:
            список элементов
        """
        return [item for item in self._items 
                if hasattr(item, 'author') and item.author == author]
    
    
    
    def __len__(self) -> int:
        """Возвращает количество элементов."""
        return len(self._items)
    
    def __iter__(self):
        """Поддержка итерации."""
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        """
        Доступ по индексу.
        
        Args:
            index: индекс элемента
        
        Returns:
            элемент типа T
        """
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if not (0 <= index < len(self._items)):
            raise IndexError(f"Индекс {index} вне диапазона")
        return self._items[index]
    
   
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Находит первый элемент, удовлетворяющий условию.
        
        Args:
            predicate: функция-условие, принимающая элемент и возвращающая bool
        
        Returns:
            первый подходящий элемент или None
        """
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """
        Возвращает список всех элементов, удовлетворяющих условию.
        
        Args:
            predicate: функция-условие, принимающая элемент и возвращающая bool
        
        Returns:
            список подходящих элементов
        """
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """
        Применяет функцию преобразования к каждому элементу.
        
        Args:
            transform: функция преобразования, принимающая T и возвращающая R
        
        Returns:
            список результатов преобразования типа R
        
        Example:
            # Преобразование TypedCollection[Book] в list[str] (названия)
            titles = collection.map(lambda b: b.title)
            
            # Преобразование в list[float] (цены со скидкой)
            prices = collection.map(lambda b: b.price * 0.9)
        """
        return [transform(item) for item in self._items]
    
    
    
    def sort_by(self, key_func: Callable[[T], any], reverse: bool = False) -> 'TypedCollection[T]':
        """
        Сортировка коллекции с использованием функции-ключа.
        
        Args:
            key_func: функция, возвращающая значение для сравнения
            reverse: если True, сортировка в обратном порядке
        
        Returns:
            self (для цепочек вызовов)
        """
        self._items.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        """
        Фильтрация коллекции с использованием функции-предиката.
        
        Args:
            predicate: функция, возвращающая True для элементов, которые нужно оставить
        
        Returns:
            self (для цепочек вызовов)
        """
        self._items = [item for item in self._items if predicate(item)]
        return self
    
    def apply(self, func: Callable[[T], None]) -> 'TypedCollection[T]':
        """
        Применяет произвольную функцию ко всем элементам коллекции.
        
        Args:
            func: функция, которая будет вызвана для каждого элемента
        
        Returns:
            self (для цепочек вызовов)
        """
        for item in self._items:
            func(item)
        return self
    

    
    def __str__(self) -> str:
        return f"{self.name}: {len(self._items)} элементов"
    
    def __repr__(self) -> str:
        return f"TypedCollection(name='{self.name}', items={len(self._items)})"



class DisplayableCollection(TypedCollection[D]):
    """
    Коллекция, хранящая только объекты, реализующие протокол Displayable.
    (то есть имеющие метод display())
    """
    pass


class ScorableCollection(TypedCollection[S]):
    """
    Коллекция, хранящая только объекты, реализующие протокол Scorable.
    (то есть имеющие метод score())
    """
    pass