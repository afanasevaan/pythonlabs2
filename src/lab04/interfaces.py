from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для объектов, которые можно вывести в строку."""
    
    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта."""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать."""
    
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с другим.
        Возвращает:
        - отрицательное число, если self < other
        - 0, если self == other
        - положительное число, если self > other
        """
        pass


class Discountable(ABC):
    """Интерфейс для объектов, на которые можно применить скидку."""
    
    @abstractmethod
    def apply_discount(self, percent: float) -> None:
        """Применяет скидку в процентах."""
        pass