# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        
        if p.val > q.val:
            p, q = q, p
        
        while node:
            if p.val <= node.val <= q.val:
                return node
            
            if p.val > node.val:
                node = node.right
                continue
                
            if q.val < node.val:
                node = node.left
                continue