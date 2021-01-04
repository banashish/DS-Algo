# reference https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/ 

class newNode():

    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None


def inOrder(root):
    if(not root):
        return 
    
    inOrder(root.left)
    print(root.key,end=" ")
    inOrder(root.right)


def insert(temp,key):
    if not temp:
        root = newNode(key)
        return

    q = []
    q.append(temp)

    while(len(q)):
        temp = q.pop(0)
        if( not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)


if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(11) 
    root.left.left = newNode(7) 
    root.right = newNode(9) 
    root.right.left = newNode(15) 
    root.right.right = newNode(8) 
 
    print("Inorder traversal before insertion:", end = " ")
    inOrder(root) 
 
    key = 12
    insert(root, key) 
 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inOrder(root)
        