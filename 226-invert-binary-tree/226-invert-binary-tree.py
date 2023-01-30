from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    stack.appendleft(node.left)
                if node.right:
                    stack.appendleft(node.right)
            
        return root