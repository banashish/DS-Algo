class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

# time complexity is O(n^2) as we have to recursively move to the end of the linked list to add new node at the end
def inputLL():
    ll = LinkedList()
    x = int(input())
    while(x != -1):
        if ll.head == None:
            ll.head = Node(x)
        else:
            temp = ll.head
            while(temp.next != None):
                temp = temp.next

            temp.next = Node(x)

        x = int(input())

    return ll.head

# Time complexity is just O(n) as we don't require any new comparison we are just storing a pointer to the end of the linkedlist


def inputLLNew():
    ll = LinkedList()
    x = int(input())
    while(x != -1):
        if ll.head == None:
            ll.head = Node(x)
            tail = ll.head
        else:
            tail.next = Node(x)
            tail = tail.next

        x = int(input())

    return ll.head



def printLL(head):
    print(">>>>>>>>>>>>>>>")
    while(head!= None):
        print(head.val)
        head = head.next
        
head = inputLLNew()
printLL(head)     

        