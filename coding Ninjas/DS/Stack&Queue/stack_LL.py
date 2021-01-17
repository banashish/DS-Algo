class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size  = 0

    def push(self,data):
        self.size+=1
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if self.size == 0:
            raise Exception('size of stack is 0')
            return
        self.size-=1
        self.head = self.head.next

    def top(self):
        if self.size == 0:
            raise Exception('size of stack is 0')
            return
        return self.head.val
    
    def isEmpty(self):
        return self.size == 0

    def sizeStack(self):
        return self.size

s = Stack()
s.push(99)
s.push(84)
a = s.top() 
print(a) 
s.pop()
s.pop()
print(s.isEmpty())
print(s.sizeStack())
s.pop()


        