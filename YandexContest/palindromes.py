# Задача 5
# Напишите программу, которая определяет, относится ли введённая строка к палиндромам.

def palindrom_check(line):
    cleaned = line.lower()
    return cleaned == cleaned[::-1]


line = input()
print('YES' if palindrom_check(line) else 'NO')
