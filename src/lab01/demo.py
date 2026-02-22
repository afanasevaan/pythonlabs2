"""
Демонстрация работы класса Book
Лабораторная работа №1: Класс и инкапсуляция
Вариант: Библиотека / Книги
"""

from model import Book

def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №1")
    print("Класс и инкапсуляция (Вариант: Книги)") 
    print("=" * 60)
    
    # 1. ДЕМОНСТРАЦИЯ СОЗДАНИЯ ОБЪЕКТОВ
    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ")
    print("-" * 40)
    
    try:
        book1 = Book("Война и мир", "Лев Толстой", 1869, 1300, 1500.0)
        book2 = Book("Преступление и наказание", "Ф. Достоевский", 1866, 672, 800.0)
        print("✓ Объекты успешно созданы")
        print(f"   {book1}")
        print(f"   {book2}")
    except Exception as e:
        print(f"✗ Ошибка при создании: {e}")
    
    # 2. ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ
    print("\n2. МАГИЧЕСКИЕ МЕТОДЫ")
    print("-" * 40)
    
    print("__str__():")
    print(f"   {book1}")
    print("\n__repr__():")
    print(f"   {repr(book1)}")
    
    # 3. ДЕМОНСТРАЦИЯ СРАВНЕНИЯ (__eq__)
    print("\n3. СРАВНЕНИЕ ОБЪЕКТОВ")
    print("-" * 40)
    
    book3 = Book("Война и мир", "Лев Толстой", 2000, 500, 500.0)
    book4 = Book("Мастер и Маргарита", "М. Булгаков", 1967, 480, 1200.0)
    
    print(f"book1 == book3: {book1 == book3} (одинаковые название и автор)")
    print(f"book1 == book4: {book1 == book4} (разные книги)")
    
    # 4. ДЕМОНСТРАЦИЯ СВОЙСТВ (Getters/Setters)
    print("\n4. РАБОТА СО СВОЙСТВАМИ")
    print("-" * 40)
    
    print(f"Текущая цена книги: {book1.price} руб.")
    book1.price = 2000.0
    print(f"Новая цена: {book1.price} руб.")
    
    # 5. ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ
    print("\n5. ПРОВЕРКА ВАЛИДАЦИИ")
    print("-" * 40)
    
    try:
        book1.price = 15000  # превышает MAX_PRICE
    except ValueError as e:
        print(f"✗ Ошибка при установке цены: {e}")
    
    try:
        book1.pages = -100
    except ValueError as e:
        print(f"✗ Ошибка при установке страниц: {e}")
    
    # 6. ДЕМОНСТРАЦИЯ АТРИБУТА КЛАССА
    print("\n6. АТРИБУТ КЛАССА")
    print("-" * 40)
    
    print(f"MAX_PRICE через класс: {Book.MAX_PRICE}")
    print(f"MAX_PRICE через экземпляр: {book1.MAX_PRICE}")
    
    # 7. ДЕМОНСТРАЦИЯ БИЗНЕС-МЕТОДОВ
    print("\n7. БИЗНЕС-МЕТОДЫ")
    print("-" * 40)
    
    print(f"Категория книги '{book1.title}': {book1.get_age_category()}")
    
    print(f"\nДорогая ли книга? {book1.is_expensive()}")
    
    # 8. ДЕМОНСТРАЦИЯ ИЗМЕНЕНИЯ СОСТОЯНИЯ
    print("\n8. ИЗМЕНЕНИЕ СОСТОЯНИЯ ОБЪЕКТА")
    print("-" * 40)
    
    print(f"Начальное состояние: {'Доступна' if book1.is_available else 'Выдана'}")
    
    book1.borrow()
    print(f"После выдачи: {'Доступна' if book1.is_available else 'Выдана'}")
    
    try:
        book1.borrow()  # пытаемся выдать снова
    except Exception as e:
        print(f"Ошибка при повторной выдаче: {e}")
    
    book1.return_book()
    print(f"После возврата: {'Доступна' if book1.is_available else 'Выдана'}")
    
    # 9. ДЕМОНСТРАЦИЯ ПРИМЕНЕНИЯ СКИДКИ
    print("\n9. ПРИМЕНЕНИЕ СКИДКИ")
    print("-" * 40)
    
    print(f"Цена до скидки: {book2.price} руб.")
    book2.apply_discount(15)
    print(f"Цена после скидки 15%: {book2.price} руб.")
    
    # 10. ДЕМОНСТРАЦИЯ НЕКОРРЕКТНОГО СОЗДАНИЯ
    print("\n10. ТЕСТЫ НА НЕКОРРЕКТНЫЕ ДАННЫЕ")
    print("-" * 40)
    
    test_cases = [
        ("Пустое название", {"title": "   ", "author": "Автор", "year": 2000, "pages": 100, "price": 500}),
        ("Год из будущего", {"title": "Книга", "author": "Автор", "year": 3000, "pages": 100, "price": 500}),
        ("Отрицательные страницы", {"title": "Книга", "author": "Автор", "year": 2000, "pages": -50, "price": 500}),
        ("Отрицательная цена", {"title": "Книга", "author": "Автор", "year": 2000, "pages": 100, "price": -100}),
        ("Слишком много страниц", {"title": "Книга", "author": "Автор", "year": 2000, "pages": 20000, "price": 500}),
    ]
    
    for description, params in test_cases:
        try:
            Book(**params)
            print(f"  [FAIL] {description} - должно было вызвать ошибку!")
        except (TypeError, ValueError) as e:
            print(f"  [OK] {description}: {e}")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)

if __name__ == "__main__":
    main()