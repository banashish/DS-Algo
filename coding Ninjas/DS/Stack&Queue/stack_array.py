class Stack:

    def __init__(self):
        self.stack = []


    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if self.isEmpty():
            raise Exception('stack passed on to function is empty.')
            return
        self.stack.pop()

    def top(self):
        if self.isEmpty():
            raise Exception('stack passed on to function is empty.')
            return
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

