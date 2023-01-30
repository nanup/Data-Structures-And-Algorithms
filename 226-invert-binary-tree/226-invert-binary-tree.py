# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Solution.recurse(self, root)
        return root
        
    def recurse(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return
        node.right, node.left = node.left, node.right
        
        Solution.recurse(self, node.right)
        Solution.recurse(self, node.left)