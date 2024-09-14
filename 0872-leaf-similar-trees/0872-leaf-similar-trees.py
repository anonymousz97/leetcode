# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        parsedRoot1 = self.parseTree(root1, [])
        parsedRoot2 = self.parseTree(root2, [])
        # print(parsedRoot1, parsedRoot2)
        if parsedRoot1 == parsedRoot2:
            return True
        return False
        
        
    def parseTree(self, root1, lst_node):
        if root1.left is None and root1.right is None:
            lst_node.append(root1.val)
            return lst_node
        if root1.left is not None:
            lst_node = self.parseTree(root1.left, lst_node)
        if root1.right is not None:
            lst_node = self.parseTree(root1.right, lst_node)
        return lst_node
        
        