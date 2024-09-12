# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root, 1)
            
    def getMaxDepth(self, root: Optional[TreeNode], max_depth: int) -> int:
        if root is None:
            return max_depth - 1
        l = self.getMaxDepth(root.left, max_depth+1)
        r = self.getMaxDepth(root.right, max_depth+1)
        return max(l, r)
        