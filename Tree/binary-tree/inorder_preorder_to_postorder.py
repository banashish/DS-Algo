# Given Inorder and Preorder traversals of a binary tree, print Postorder traversal.

# Example:

# Input:
# Inorder traversal in[] = {4, 2, 5, 1, 3, 6}
# Preorder traversal pre[] = {1, 2, 4, 5, 3, 6}

# Output:
# Postorder traversal is {4, 5, 2, 6, 3, 1}
# References  https://www.geeksforgeeks.org/print-postorder-from-given-inorder-and-preorder-traversals/


class Node:
    def __init__(self,data):
        self.data = data
        self.left = left
        self.right = right

def search(arr,key,n):
    for i in range(n):
        if arr[i] == key:
            return i

    return -1


def postOrderTraversal(In,Pre,n):
    root = search(In,Pre[0],n)

    if(root != 0):
        postOrderTraversal(In[0:root],Pre[1:n],root)

    if(root != n-1):
        postOrderTraversal(In[root+1:n],Pre[root+1:n],n-1-root)

    print(Pre[0],end=" ")

In = [ 4, 2, 5, 1, 3, 6 ]
Pre = [ 1, 2, 4, 5, 3, 6 ]
n = len(In)
 
print("Postorder traversal ")
 
postOrderTraversal(In, Pre, n)