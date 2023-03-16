# Алгоритм

def hanoi(n=1, source='A', target='B', auxiliary='C'):
    if n == 1:
        print('Переместить диск 1 с', source, 'на', target)
        return
    hanoi(n - 1, source, auxiliary, target)
    print('Переместить диск', n, 'с', source, 'на', target)
    hanoi(n - 1, auxiliary, target, source)


n = int(input('\tВведите количество дисков: '))
# s, t, a = input('Введите название первой башни: '), input('Введите название второй башни: '), \
#     input('Введите название третьей башни: ')
# hanoi(n, s, t, a)
hanoi(n)


# Модификация со счетчиком
count = 1


def hanoi_с(count, n=1, source='A', target='B', auxiliary='C'):
    if n == 1:
        print(count, ': Переместить диск 1 с', source, 'на', target)
        count += 1
        return count

    count = hanoi_с(count, n - 1, source, auxiliary, target)
    print(count, ': Переместить диск', n, 'с', source, 'на', target)
    count += 1
    count = hanoi_с(count, n - 1, auxiliary, target, source)
    return count


n = int(input('\tВведите количество дисков: '))
hanoi_с(count, n)
