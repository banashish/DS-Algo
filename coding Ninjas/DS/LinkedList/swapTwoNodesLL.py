from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapIJ(head, M, N) :
    if head is None:
        return head

    prev1, curr1, next1, prev2, curr2, next2 = None, None, None, None, None, None
    maxNum = max([M,N])
    temp = head
    for i in range(maxNum+1):
        if head is None:
            return head

        if i == M-1 or i == N-1:
            if prev1 is None:
                prev1 = head
                curr1 = head.next
                next1 = head.next.next
            else:
                prev2 = head
                curr2 = head.next
                next2 = head.next.next

            head = head.next




    


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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = swapIJ(head, m, n)
    printLinkedList(newHead)

    t -= 1