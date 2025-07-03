# Задача 1. Вывести YES, если все слова начинаются с указанных букв, иначе NO.
letters = ('а', 'б', 'в')
N = int(input())
for _ in range(N):
    word = input().lower()
    if not word.startswith(letters):
        print('NO')
        break
else:
    print('YES')
