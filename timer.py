import time
from functools import wraps


def timer(func):
    """Декоратор для измерения времени выполнения функции."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Начальное время
        result = func(*args, **kwargs)  # Вызов целевой функции
        end_time = time.perf_counter()  # Конечное время
        elapsed_time = end_time - start_time  # Вычисление затраченного времени

        # Вывод результата в секундах с округлением до 4 знаков
        print(f"Функция {func.__name__!r} выполнилась за {elapsed_time:.8f} секунд")
        return result

    return wrapper
