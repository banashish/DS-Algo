class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self,data):
        if(self.size==0):
            self.front+=1
        self.queue.append(data)
        self.size+=1
        self.rear+=1

    def top(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        self.front-=1
        self.size-=1
        if self.size == 0:
            self.queue = []
            self.front = -1
            self.rear = -1


q = Queue()
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


    
