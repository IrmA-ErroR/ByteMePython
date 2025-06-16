def simple_generator():
       yield 1
       yield 2
       yield 3


def fibonacci(a=0, b=1, n=3):
    for i in range(n):
        yield a
        a, b = b, a + b


gen = simple_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Генераторное выражение
squares = (i**2 for i in range(1, 4))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares, "None"))

print('Числа Фибоначчи: ')
for num in fibonacci(n=10):
    print(num)
