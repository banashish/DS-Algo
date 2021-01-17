class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class Queue_LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,data):
        if self.isEmpty():
            self.head = Node(data)
            self.tail = self.head
            self.size+=1
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.size+=1

    def top(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        return self.head.val

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def dequeue(self):
        if self.isEmpty():
            raise Exception('queue is empty')
        self.head = self.head.next
        self.size-=1


q = Queue_LL()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(7)
x = q.top()
print(x)


