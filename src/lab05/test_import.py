import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("Путь поиска:", sys.path[:3])
print("Пытаюсь импортировать...")

try:
    from lab04.interfaces import Printable
    print("✅ lab04.interfaces работает")
except ModuleNotFoundError as e:
    print(f"❌ Ошибка: {e}")
    
    try:
        from interfaces import Printable
        print("✅ interfaces (без lab04) работает")
    except ModuleNotFoundError as e2:
        print(f"❌ И так не работает: {e2}")