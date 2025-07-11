def check_brackets(string):
    temp_queue = []
    for i in range(len(string)):
        if string[i] == '(':
            temp_queue.append('(')
        if string[i] == ')':
            if temp_queue:
                temp_queue.pop()
            else:
                return 'Wrong brackets'

    if temp_queue:
        # print(temp_queue)
        return 'Wrong brackets'
    else:
        return 'OK'


check_it = input()
print(check_brackets(check_it))
