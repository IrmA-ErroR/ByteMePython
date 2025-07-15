import asyncio
# Заменить строку через asyncio
# Напишите функцию main() в которой должна отрабатывать функция replace_async, которая принимает строку s, слово для замены old, и новое слово new. Необходимо асинхронно заменить все вхождения слова old в строке s на new и вернуть новую строку.

async def replace_async(s, old, new):
    new_string = s.replace(old, new)
    await asyncio.sleep(0)

    return new_string


if __name__ == "__main__":
    # s, old, new = input('Введите строку: '), input('Введите строку, которую хотите заменить: '), input('Введите строку для замены: ')
    s = 'hello world'
    old = 'world'
    new = 'Python'
    print(asyncio.run(replace_async(s, old, new)))
