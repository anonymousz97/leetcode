# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def process(self, root: Optional[TreeNode], cur_depth):
        if root is None:
            return
        if cur_depth > len(self.lst_see):
            self.lst_see.append(root.val)
        self.process(root.right, cur_depth+1)
        self.process(root.left, cur_depth+1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.lst_see = []
        self.process(root, 1)
        return self.lst_see
        
        