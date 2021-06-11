# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        answer = []
        node = root
        l = 1
        queue = Queue()
        level = Queue()
        queue.put(root)
        level.put(1)
        while not queue.empty():
            print("hi")
            child = queue.get()
            d = queue.get()
            # if d > l:
            #     answer.append(node.val)
            #     l = d
            #     node = child
            # else:
            #     node = child
            if child.left:
                queue.put(child.left)
                level.put(d+1)
            if child.right:
                queue.put(child.right)
                level.put(d+1)
            
        print(answer)
        



from queue import Queue
queue = Queue()
queue.put(1)
queue.put(2)
x = queue.get()
print(x,queue.empty())