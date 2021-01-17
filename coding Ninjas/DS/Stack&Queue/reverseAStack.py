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
    
    def printStack(self):
        print(self.stack)

s1 = Stack()
s2 = Stack()
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(6)

def solution(s1,s2):
    while not s1.isEmpty():
        x = s1.pop()
        count = 0 
        while not s2.isEmpty():
            s1.push(s2.pop())
            count+=1
        s2.push(x)
        while count > 0:
            s2.push(s1.pop())
            count-=1

    while not s2.isEmpty():
        s1.push(s2.pop())

solution(s1,s2)


print(s1.top())




