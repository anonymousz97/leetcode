# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lst_p = self.findDescendant(root, p, [])
        #print("p",lst_p)
        lst_q = self.findDescendant(root, q, [])
        #print("q",lst_q)
        while len(lst_q) != max(len(lst_q), len(lst_p)):
            lst_q.append(q)
        while len(lst_p) != max(len(lst_q), len(lst_p)):
            lst_p.append(p)
        for idx, (i,j) in enumerate(zip(lst_p, lst_q)):
            if i != j:
                return lst_p[idx-1]
    def findDescendant(self, root, p, lst_path):
        if not root:
            return []
        
        if root.val == p.val:
            lst_path.append(root)
            return lst_path
        
        length = len(lst_path)
        lst_path.append(root)
        length = len(lst_path)
        # print("Current node ", root.val, len(lst_path))
        # print("-"*30)
        path = self.findDescendant(root.left, p, lst_path)
        if path != []:
            return path
        lst_path = lst_path[:length]
        path = self.findDescendant(root.right, p, lst_path)
        return path
        
        
        