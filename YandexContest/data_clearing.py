# Задача 4
# Напишите программу, которая обрабатывает лог-файл, состоящий из строк, и:
# удаляет две решётки ## в начале строки, если они есть;
# удаляет всю строку, если она заканчивается на @@@.

# Ввод продолжается, пока не встретится пустая строка.
text = []

while True:
    line = input()
    if not line:
        break
    text.append(line)


for line in text:
    if line.startswith('##'):
        line = line[2:]
    if line.endswith('@@@'):
        continue
    print(line)
