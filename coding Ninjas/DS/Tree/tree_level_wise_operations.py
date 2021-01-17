class TreeNode:
    def __init__(self,data = 0):
        self.val = data
        self.children = []

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
        x = self.head
        self.head = self.head.next
        self.size-=1
        return x.val


def construct():
    queue = Queue_LL()
    print("enter root node")
    root = TreeNode(input().strip())
    queue.enqueue(root)
    while not queue.isEmpty():
        try:
            frontNode = queue.dequeue()
            print("enter number of children for "+ str(frontNode.val))
            for i in range(int(input().strip())):
                print("enter " + str(i+1) + "th child for " + str(frontNode.val))
                childNode = TreeNode(input().strip())
                frontNode.children.append(childNode)
                queue.enqueue(childNode)
        except:
            print('Error occurred')
            raise

    return root

def printTree(root):
    queue_print = Queue_LL()
    queue_print.enqueue(root)
    while not queue_print.isEmpty():
        try:
            child_node = queue_print.dequeue()
            s = str(child_node.val) + ': '
            for child in child_node.children:
                s = s + str(child.val) + ','
                queue_print.enqueue(child)
            print(s)
            
        except:
            print('Error occurred')
            raise


def number_nodes(root):
    if root is None:
        return 0
    count = 1
    for child in root.children:
        count+=number_nodes(child)

    return count

def sum_of_nodes(root):
    if root is None:
        return None
    value = int(root.val)
    for child in root.children:
        value+=int(sum_of_nodes(child))

    return value

def largest_node(root):
    if root is None:
        return -1
    value = [int(root.val)]
    for child in root.children:
        value.append(int(largest_node(child)))
    return max(value)

def height_of_tree(root):
    if root is None:
        return 0
    height = 1
    answer = 0
    for child in root.children:
        x = height_of_tree(child)
        if(x > answer):
            answer = x 
    
    return height + answer

def height_alternate(root):
    if root is None:
        return 0
    
    if len(root.children) == 0:
        return 1

    max_height = 0
    for child in root.children:
        max_height = max(max_height,height_alternate(child))

    return max_height + 1






tree = construct()
printTree(tree)
print(">>>>>>>>>>>>>>")
print(number_nodes(tree))
print(">>>>>>>>>>>>>>")
print(sum_of_nodes(tree))
print(">>>>>>>>>>>>>>")
print(largest_node(tree))
print(">>>>>>>>>>>>>>")
print(height_of_tree(tree))



