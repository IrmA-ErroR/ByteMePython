# Задача 6
# 1. Посчитать сколько раз встретилось слово "зайка" в введенных предложениях.
# 2. Для каждой строки нужно найти положение первого зайки.

focus_word = 'зайка'
N = int(input())
# count = 0
text = [input().lower() for _ in range(N)]

# for i in range(N):
#     line = input()
#     count += line.lower().count(focus_word)
# print(count)

for line in text:
    if focus_word in line.split():
        print(line.index(focus_word) + 1)
    else:
        print('Заек нет =(')
