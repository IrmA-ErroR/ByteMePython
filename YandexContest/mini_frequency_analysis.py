letter_count = {}

while True:
    line = input().lower()
    if line == 'финиш':
        break
    for char in line:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

if letter_count:
    max_count = max(letter_count.values())
    result = min(char for char, count in letter_count.items() if count == max_count)
    print(*result)
else:
    print()
