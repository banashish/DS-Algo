from sys import stdin
class Node:
    def __init__(self,value = 0):
        self.val = value
        self.next = None

def takeInput():
    head = None
    tail = None

    datas = list(map(int,input().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

        i+=1

    return head


def printLinkedList(head) :

    while head is not None :
        print(head.val, end = " ")
        head = head.next

    print()

def findLength(head):
    length = 0
    while head is not None:
        length+=1
        head = head.next

    return length


head = takeInput()
print(">>>>>>>>>>")
printLinkedList(head)
print(">>>>>>>>>>")
print(findLength(head))



        