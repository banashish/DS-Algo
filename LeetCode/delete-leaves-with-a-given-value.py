#Link = https://leetcode.com/problems/delete-leaves-with-a-given-value/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        return self.dfs(root,target)
        
    def dfs(self,root,target):
        if root is None:
            return
        
        self.dfs(root.left,target)
        self.dfs(root.right,target)
        
        if root.left:
            if root.left.left is None and root.left.right is None and root.left.val == target:
                root.left = None
                
        if root.right:
            if root.right.left is None and root.right.right is None and root.right.val == target:
                root.right = None
                
        if root.left is None and root.right is None and root.val == target:
            root = None
                
        return root