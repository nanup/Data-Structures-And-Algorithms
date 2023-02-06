from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque()
        result = []
        
        stack.append(root)
        
        while stack:
          level = len(stack)
          levelResult = []
          
          for _ in range(level):
            node = stack.pop()
            if node:
              stack.appendleft(node.left)
              stack.appendleft(node.right)
              levelResult.append(node.val)
              
          if levelResult:  
            result.append(levelResult)
          
        return result