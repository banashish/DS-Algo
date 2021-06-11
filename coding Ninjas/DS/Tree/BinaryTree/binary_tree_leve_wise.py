class BinarytreeNode:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right= None

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

class BinaryTreeLevelWise:
    def construct(self):
        queue = Queue_LL()
        
        print("enter root node for your tree")
        value = int(input().strip())
        if value == -1:
            return
        root = BinarytreeNode(value)
        queue.enqueue(root)

        while not queue.isEmpty():
            try:
                node = queue.dequeue()
                
                print("enter left node value for" + str(node.data))

                left = int(input().strip())
                if(left != -1):
                    leftNode = BinarytreeNode(left)
                    queue.enqueue(leftNode)
                    node.left = leftNode

                print("enter right node value for" + str(node.data))

                right = int(input().strip())
                if(right != -1):
                    rightNode = BinarytreeNode(right)
                    queue.enqueue(rightNode)
                    node.right = rightNode

            except:
                print("Error occured")
                raise

        return root

    def printTree(self,root):
        queue = Queue_LL()
        queue.enqueue(root)
        
        while not queue.isEmpty():
            s = ''
            node = queue.dequeue()
            s = s + str(node.data) + ': '
            if node.left:
                s = s + 'L' + str(node.left.data) + ' , '
                queue.enqueue(node.left)
            if node.right:
                s = s + 'R' + str(node.right.data) + ' , '
                queue.enqueue(node.right)

            print(s)

    def countNodes(self,root):
        if root is None:
            return 0
        answer = 1
        answer += self.countNodes(root.left)
        answer += self.countNodes(root.night)

        return answer

    def isNodePresent(self,root,value):
        if root is None:
            return False
        
        if root.data  == value:
            return True

        ans = self.isNodePresent(root.left,value) or self.isNodePresent(root.right,value)
        return ans

        

tree = BinaryTreeLevelWise()
root = tree.construct()
print(">>>>>>>>>>>>>>>>>>>>>\n")
tree.printTree(root)
print(">>>>>>>>>>>>>>>>>>>>>\n")
print(tree.countNodes(root))
print(">>>>>>>>>>>>>>>>>>>>>\n")
print(tree.isNodePresent(root,5))
