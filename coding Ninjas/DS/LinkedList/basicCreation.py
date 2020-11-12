class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

def printList(head):
    while head != None:
        print(head.val,end = "\n")
        head = head.next 


ll = LinkedList()
node1 = Node(5)
node2 = Node(6)
node3 = Node(40)
ll.head = node1
node1.next = node2
node2.next = node3

printList(ll.head)
printList(ll.head)