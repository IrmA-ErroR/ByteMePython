import random
class Stack:
    # items = []
    def __int__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:
    # stack_enqueue, stack_dequeue = Stack(), Stack()
    def __int__(self):
        self.item_enqueue = Stack()
        self.item_dequeue = Stack()

    def is_empty(self):
        return self.stack_enqueue.is_empty() and self.stack_dequeue.is_empty()

    def enqueue(self, item):
        self.stack_enqueue.push(item)

    def dequeue(self):
        if self.stack_enqueue:
            if self.stack_dequeue.is_empty():
                while not self.stack_enqueue.is_empty():
                    self.stack_dequeue.push(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def peek(self):
        if self.stack_enqueue:
            if self.stack_dequeue.is_empty():
                while not self.stack_enqueue.is_empty():
                    self.stack_dequeue.push(self.stack_enqueue.pop())
        return self.stack_dequeue[-1]

    def size(self):
        return self.stack_enqueue.size()


my_queue = Queue()
for _ in range(10):
    n = random.randint(1, 1000)
    my_queue.enqueue(n)

print('Queue:', my_queue, my_queue.size(), '\n', [my_queue.peek() for i in range(my_queue.size()-1)])
while not my_queue.is_empty():
    print(my_queue.dequeue(), end=' ')


my_stack = Stack()
for _ in range(10):
    n = random.randint(1, 2000)
    my_stack.push(n)




print('Queue:', my_queue, my_queue.size(), '\n', [my_queue.dequeue() for i in range(my_queue.size()-1)])
while not my_queue.is_empty():
    print(my_queue.dequeue(), end=' ')
# [print(my_queue.peek())for i in range(my_queue.size()-1)])

print('\nStack:\n', my_stack)
