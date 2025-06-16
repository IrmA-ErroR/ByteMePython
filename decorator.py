import time
from functools import lru_cache

def normalize_decorator(func):
    def wrapper(number=1, *args, **kwargs):
        start_time = time.time()

        print(f"Начало нормализации: число={number}, args={args}, kwargs={kwargs}")
        result = func(number, *args, **kwargs)

        end_time = time.time()
        print(f"Нормализация завершена. Время выполнения: {end_time - start_time:.4f} сек.")

        return result
    return wrapper


@normalize_decorator
def my_normalization(number=1, *args, **kwargs):
    '''Функция нормализации параметры:
    number - число, границы диапазона нормализации min и max, '''
    numbers = []
    normalized_n = []

    min_val = kwargs.get('min', 0)
    max_val = kwargs.get('max', 1)
    scale = kwargs.get('scale', 1)
    numbers = [number] + list(args) if args else [number]

    for num in numbers:
        if len(numbers) > 1:
            min_input = min(numbers)
            max_input = max(numbers)
        else:
            min_input = min_val
            max_input = number if number != 0 else 1

        if max_input == min_input: # Все числа одинаковые
            normalized_num = max_val
        else:
            normalized_num = ((num - min_input) / (max_input - min_input)) * scale
            normalized_num = max(min_val, min(max_val, normalized_num))

        normalized_n.append(normalized_num)

    time.sleep(10)

    return normalized_n


def cache_decorator(func):
    caches = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items())) # ключ из аргументов (кортеж + frozenset для kwargs)
        if key not in caches:
            caches[key] = func(*args, **kwargs)
            # print(caches)
        return caches[key]
    print(caches)
    return wrapper


@cache_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=None)  # None — без ограничения размера
def fibonacci_1(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


# Декоратор логирования времени выполнения
print(my_normalization(5, 10, 15, min=0, max=10))
print(my_normalization(3, scale=100))


# Декоратор кеширования
print(fibonacci(11))  # Вычисляется
print(fibonacci(11))  # Берётся из кэша

print(fibonacci_1(11))
