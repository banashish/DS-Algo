#references https://www.geeksforgeeks.org/deletion-binary-tree/

class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inOrder(temp):
    if(not temp):
        return 
    
    inOrder(temp.left)
    print(temp.data,end=" ")
    inOrder(temp.right)

def delete(root,key):
    if root is None:
        return None

    if root.left == None and root.right == None:
        if root.data == key:
            return None
        else:
            return root

    q = []
    q.append(root)
    delete_node = None
    while(len(q) > 0):
        temp = q.pop(0)
        if(temp.data == key):
            delete_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if delete_node:
        x = temp.data
        deleteDeepestNode(root,temp)
        delete_node.data = x
    
    return root

def deleteDeepestNode(root,d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return 
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)

        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

if __name__=='__main__': 
    root = Node(10) 
    root.left = Node(11) 
    root.left.left = Node(7) 
    root.left.right = Node(12) 
    root.right = Node(9) 
    root.right.left = Node(15) 
    root.right.right = Node(8) 
    print("The tree before the deletion:") 
    inOrder(root) 
    key = 11
    root = delete(root, key) 
    print() 
    print("The tree after the deletion;") 
    inOrder(root) 