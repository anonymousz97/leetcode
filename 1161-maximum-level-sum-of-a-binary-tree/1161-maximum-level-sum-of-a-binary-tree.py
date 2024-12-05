# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.dct_value = {}
        self.process(root, 1)
        return max(self.dct_value, key=lambda k: sum(self.dct_value[k]))
        
    def process(self, root: Optional[TreeNode], cur_length):
        if root is None:
            return 
        if cur_length in self.dct_value.keys():
            self.dct_value[cur_length].append(root.val)
        else:
            self.dct_value[cur_length] = [root.val]
        self.process(root.right, cur_length+1)
        self.process(root.left, cur_length+1)
    
        