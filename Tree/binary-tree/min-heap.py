import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxSize = maxsize
        self.size = 0
        self.Heap = [0]*(maxsize+1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def insert(self, element):
        if self.size >= self.maxSize:
            return
        self.size+=1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] < self.Heap[self.__parent(current)]:
            self.__swap(current,self.__parent(current))
            current = self.__parent(current)
    
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-=1
        self.__minHeapTree(self.FRONT)
        return popped

    def printHeap(self):
        for i in range(1,(self.size//2)+1):
            print("Parent : " + str(self.Heap[i]) + ", Left child : " + str(self.Heap[2*i]) + ", Right child : " + str(self.Heap[(2*i)+1]))

    def __minHeapTree(self, pos):
        if not self.isLeaf(pos):
            if(self.Heap[pos] > self.Heap[self.__leftChild(pos)] or self.Heap[pos] > self.Heap[self.__rightChild(pos)]):
                if self.Heap[self.__leftChild(pos)] < self.Heap[self.__rightChild(pos)]:
                    self.__swap(pos,self.__leftChild(pos))
                    self.__minHeapTree(self.__leftChild(pos))
                else:
                    self.__swap(pos,self.__rightChild(pos))
                    self.__minHeapTree(self.__rightChild(pos))

    def __parent(self,pos):
        return pos//2

    def __swap(self, fpos, spos):
        self.Heap[fpos] , self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def __leftChild(self,pos):
        return 2 * pos

    def __rightChild(self, pos):
        return (2*pos) + 1
        



if __name__ == '__main__':
    minheap = MinHeap(10)
    minheap.insert(5)
    minheap.insert(3)
    minheap.insert(17)
    minheap.insert(10)
    minheap.insert(84)
    minheap.insert(19)
    minheap.insert(6)
    minheap.insert(22)
    minheap.insert(9)
    minheap.printHeap()