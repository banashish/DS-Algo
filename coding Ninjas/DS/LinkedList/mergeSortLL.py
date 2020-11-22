from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def midPoint(head) :
    if head is None:
        return ''
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow 

def mergeTwoSortedLinkedLists(head1,head2):
    if(head1 is None):
        return head2
    
    if(head2 is None):
        return head1
        
    head3 = None
    tail3 = None
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            if head3 == None:
                head3 = head1
                tail3 = head1
                head1 = head1.next
            else:
                tail3.next = head1
                tail3 = head1
                head1 = head1.next
        else:
            if head3 == None:
                head3 = head2
                tail3 = head2
                head2 = head2.next
            else:
                tail3.next = head2
                tail3 = head2
                head2 = head2.next

    if head1 is not None:
        tail3.next = head1

    if head2 is not None:
        tail3.next = head2

    return head3

def mergeSort(head) :
    if(head is None or head.next is None):
        return head

    mid = midPoint(head)
    head1 = head
    head2 = mid.next
    mid.next = None

    return mergeTwoSortedLinkedLists(head1,head2)



#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1