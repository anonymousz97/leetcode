# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.maxZigZag(root.left, True, 0), self.maxZigZag(root.right, False, 0))
    
    def maxZigZag(self, root: Optional[TreeNode], isLeft: bool, depth: int):
        if not root:
            return depth
        
        if isLeft:
            depth = max(
                depth,
                self.maxZigZag(root.right, False, depth + 1),
                self.maxZigZag(root.left, True, 0)
            )
        else:
            depth = max(
                depth,
                self.maxZigZag(root.left, True, depth + 1),
                self.maxZigZag(root.right, False, 0)
            )
        return depth
            
            
        