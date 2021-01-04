# inorder traversal of binary tree using stack
# refernces https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root):
    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            print(current.data,end=" ")
            current = current.right

        else:
            break

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
inorder(root) 