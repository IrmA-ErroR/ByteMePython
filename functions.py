import time

def greate_user(name, age, city='Москва'):
    '''Функции с позиционными и именованными аргументами.
    Принимает на вход: имя (name), возраст (age) и город (city).'''

    return '\nПользователь:' + name + '\n\tвозраст:'+ str(age) + '\n\tгород:' + city


def calculate_sum(*args):
    '''Произвольные аргументы (*args)
    Функция принимает на вход произвольное количество чисел и возвращает их сумму.
    Используйте *args.
    Добавьте проверку, что все аргументы — числа (иначе вызывайте TypeError).'''

    try:
         return sum(args)
    except TypeError:
        return 'Некорректные ввод'


def create_user_profile(**kwargs):
    '''Произвольные именованные аргументы (**kwargs)
    Функция принимает произвольные именованные аргументы (**kwargs) и возвращает словарь с данными пользователя.
    Обязательные поля: username и email (если их нет, ошибка ValueError).
    Остальные поля добавляются в словарь как есть.'''

    if 'username' not in kwargs or 'email' not in kwargs:
        raise ValueError('Отсутствуют username и email')

    return kwargs


def log_arguments(*args, **kwargs):
    print('Произвольные аргументы:\n\t', args)
    print('Произвольные именованные аргументы:\n\t', kwargs)
    return ''


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


print(greate_user("Анна", 20)) # позиционные аргументы
print(greate_user(age=30, name="Иван", city="Санкт-Петербург"))  # именованные аргументы

print(calculate_sum(1, 2, 3)) # произвольные аргументы (*args)
print(calculate_sum(1, '2', 3))

print(create_user_profile(username="alex", email="alex@mail.com")) # произвольные именованные аргументы (**kwargs)
print(create_user_profile(username="max", email="max@yandex.ru", age=25, city="Москва"))
# print(create_user_profile(username="petya")) # ValueError

print(log_arguments(1, 2, 3, name="Alex", age=30))

# Анонимные функции (lambda)
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

names = ["Анна", "Иван", "Мария", "Петр"]
long_names = list(filter(lambda name: len(name) > 4, names))
print(*long_names)

# Декоратор
print(my_normalization(5, 10, 15, min=0, max=10))
print(my_normalization(3, scale=100))
print(my_normalization())
