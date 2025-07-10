# Создание списка из 5 элементов
my_list = [1, 2, '3', '!4', [5]]
print(*my_list)

# Добавление элемента (append, insert)
my_list.append(6)
my_list.insert(2, 3)
print(my_list)
# Удаление элемента (remove, pop, del)

my_list.remove(6)
popped_element = my_list.pop(3)
del(my_list[3:])

print(my_list)
print(popped_element)

# Срезы (list[1:4], list[::-1])
print(my_list[1:3])
print(my_list[::-1])

# Поиск (in, .index())
if 1 in my_list:
    my_list.append(4)
    print(my_list)

# Замена элемента по индексу
my_list[2] = '1'
print(*my_list)
