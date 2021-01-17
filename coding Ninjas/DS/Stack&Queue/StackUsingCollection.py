# stack using dequeue it provides append and pop aperation in O(1) time

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

stack.pop()

x = list(stack)
print(x)


# stack using LIFO queue

from queue import LifoQueue

stack = LifoQueue(maxsize= 3)

stack.put('a')
stack.put('b')
stack.put('c')
print(stack.full())
print(stack.qsize())
stack.get()

