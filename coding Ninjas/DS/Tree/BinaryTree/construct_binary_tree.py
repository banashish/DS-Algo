class BinarytreeNode:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right= None

class BinaryTree:
    def construct(self):
        root = BinarytreeNode(5)
        node1 = BinarytreeNode(44)
        node2 = BinarytreeNode(32)
        node3 = BinarytreeNode(56)
        node4 = BinarytreeNode(67)
        root.left = node1
        root.right = node2
        node1.left = node3
        node1.right = node4
        
        return root

    def takeInput(self):
        print("enter your node")
        ans = int(input().strip())
        if(ans == -1):
            return None

        node = BinarytreeNode(ans)
        node.left = self.takeInput()
        node.right = self.takeInput()

        return node

    def printTree(self,root):
        s = ''
        if(root == None):
            return
        s = s + str(root.data) + ': '
        if root.left:
            s = s + str(root.left.data) + ',' 
        if root.right:
            s = s + str(root.right.data) + ',' 
        print(s)
        self.printTree(root.left)
        self.printTree(root.right)
        


tree = BinaryTree()
root = tree.takeInput()
tree.printTree(root)