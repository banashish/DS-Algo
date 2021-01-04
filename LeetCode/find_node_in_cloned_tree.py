# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

# Follow up: Solve the problem if repeated values on the tree are allowed.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1 = []
        q2 = []
        q1.append(original)
        q2.append(cloned)
        
        while(len(q1)):
            temp1 = q1.pop(0)
            temp2 = q2.pop(0)
            if temp1 == target:
                return temp2
            if temp1.left:
                if temp1.left == target:
                    return temp2.left
                else:
                    q2.append(temp2.left)
                    q1.append(temp1.left)
            if temp1.right:
                if temp1.right == target:
                    return temp2.right
                else:
                    q2.append(temp2.right)
                    q1.append(temp1.right)
        