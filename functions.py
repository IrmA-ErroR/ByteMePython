
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
    users_profiles = {}

    if 'username' not in kwargs or 'email' not in kwargs:
        raise ValueError('Отсутствуют username и email')

    return kwargs


print(greate_user("Анна", 20)) # позиционные аргументы
print(greate_user(age=30, name="Иван", city="Санкт-Петербург"))  # именованные аргументы

print(calculate_sum(1, 2, 3)) # произвольные аргументы (*args)
print(calculate_sum(1, '2', 3))

print(create_user_profile(username="alex", email="alex@mail.com")) # произвольные именованные аргументы (**kwargs)
print(create_user_profile(username="max", email="max@yandex.ru", age=25, city="Москва"))
print(create_user_profile(username="petya"))  # ValueError
