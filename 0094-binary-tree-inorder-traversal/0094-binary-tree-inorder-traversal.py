# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.process(root, lst)
        return lst
    
    def process(self, root: Optional[TreeNode], lst: List[int]):
        if root:
            self.process(root.left, lst)
            lst.append(root.val)
            self.process(root.right, lst)
        
        