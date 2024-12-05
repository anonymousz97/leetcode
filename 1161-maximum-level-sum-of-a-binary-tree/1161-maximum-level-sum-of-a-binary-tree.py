# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.dct_value = {}
        queue = [root]
        cur_length = 0
        max_length = 0
        max_value = -float(inf)
        while queue:
            cur_length += 1
            lst_node = []
            sum_idx = 0
            for i in queue:
                if i is not None:
                    sum_idx += i.val
                    if i.left is not None:
                        lst_node.append(i.left)
                    if i.right is not None:
                        lst_node.append(i.right)
            if sum_idx > max_value:
                max_value = sum_idx
                max_length = cur_length
            queue = lst_node
        return max_length
                
                
            
    
        