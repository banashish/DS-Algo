class Stack:

    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)

    def pop(self):
        if self.isEmpty():
            raise Exception('stack passed on to function is empty.')
            return
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            raise Exception('stack passed on to function is empty.')
            return
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

expression = '(()()()}'


def Solution(expression):
    stack = Stack()

    if len(expression) == 0:
        return True

    for i in expression:
        if i == '(' or i == '{':
            stack.push(i)

        else:
            last = stack.pop()
            if (last == '(' and i != ')') or (last == '{' and i != '}'):
                return False
            
    if stack.isEmpty() == False:
        return False

    return True

answer = Solution(expression)
print(answer)

