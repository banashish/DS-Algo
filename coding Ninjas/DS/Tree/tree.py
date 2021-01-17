class TreeNode:
    def __init__(self,data = 0):
        self.val = data
        self.children = []

# root = TreeNode(4)
# node1 = TreeNode(2)
# node2 = TreeNode(5)4

# node3 = TreeNode(6)
# node4 = TreeNode(7)
# root.children.append(node1)
# root.children.append(node2)
# root.children.append(node3)
# node2.children.append(node4)

def takeinput():
    print("enter next node data")
    root = TreeNode(int(input().strip()))
    print("enter number of childs for",root.val)
    number = int(input().strip())
    for i in range(number):
        child = takeinput()
        root.children.append(child)
    return root

def printtree(root):
    s = str(root.val) +  ':'
    for child in root.children:
        s = s + str(child.val) + ','
    print(s,end="\n")
    for child in root.children:
        printtree(child)





def construct():
    root = takeinput()
    printtree(root)


    

construct()