def remove_comments(line):
    """Удаляет комментарии из строки (всё, что после #)"""
    return line.split('#')[0]


programm = []

while True:
    line = input().rstrip('\n')
    if not line:
        break
    programm.append(line)

for line in programm:
    code = remove_comments(line)
    if code:
        print(code)
