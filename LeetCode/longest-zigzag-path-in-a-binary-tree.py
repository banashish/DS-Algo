# Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        ans = self.dfs(root)
        return ans['maxLen']
        
    def dfs(self,root):
        if root is None:
            return {
                'maxLen' : 0,
                'maxLeft' : -1,
                'maxRight': -1
            }
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        ansDict = {}
        
        ansDict['maxLeft'] = left['maxRight'] + 1
        ansDict['maxRight'] = right['maxLeft'] + 1
        ansDict['maxLen'] = max(left['maxLen'],right['maxLen'],ansDict['maxLeft'],ansDict['maxRight'])
        
        return ansDict