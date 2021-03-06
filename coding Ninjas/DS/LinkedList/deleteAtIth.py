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

def deleteAtIth(head,target):
    if(target == 0):
        return head.next
    temp1 = head
    for i in range(target-1):
        if(temp1 == None):
            break
        temp1 = temp1.next
    if(temp1 != None):
        temp = temp1.next.next
        temp1.next = temp
    return head 
    



head = takeInput()
print(">>>>>>>>>>")
printLinkedList(head)
print(">>>>>>>>>>")
head = deleteAtIth(head,3)
print(">>>>>>>>>>")
printLinkedList(head)



        